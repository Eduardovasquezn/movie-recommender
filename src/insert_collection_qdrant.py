import pandas as pd
from langchain_google_vertexai import VertexAIEmbeddings
from qdrant_client import QdrantClient

df_anime = pd.read_csv('./data/df_anime_sample.csv')
df_anime.columns

df_users_with_rating = pd.read_csv('./data/df_users_with_ratings_sample.csv')
df_users_with_rating.columns

embeddings_model = VertexAIEmbeddings(model_name="textembedding-gecko@003")

text = "This is an example?"

len(embeddings_model.embed_query(text))

import qdrant_client
import os
from dotenv import load_dotenv
from qdrant_client import models
load_dotenv()

qdrant_host = os.getenv('QDRANT_HOST')
qdrant_api_key = os.getenv('QDRANT_API_KEY')
qdrant_collection_name = os.getenv("QDRANT_COLLECTION_NAME")

client_connection = QdrantClient(
    qdrant_host,
    api_key=qdrant_api_key,
    timeout=50
)

qdrant_vector_config = qdrant_client.http.models.VectorParams(
    size=768,
    distance=qdrant_client.http.models.Distance.COSINE
)
client_connection.create_collection(
    collection_name=qdrant_collection_name,
    vectors_config=qdrant_vector_config,
    shard_number=2
)

from langchain_community.vectorstores.qdrant import Qdrant

vector_store = Qdrant(
    client=client_connection,
    collection_name=qdrant_collection_name,
    embeddings=embeddings_model
)

# Function to generate embeddings
def generate_embeddings(text, embeddings_model=embeddings_model):
    vector_embeddings = embeddings_model.embed_query(text)
    return vector_embeddings

df_anime["vector_embeddings"] = df_anime['sypnopsis'].apply(generate_embeddings)

payloads = df_anime[['MAL_ID', 'Name', 'Japanese name', 'Genres', 'Score', 'poster_url']].to_dict('records')

client_connection.upsert(
    collection_name=qdrant_collection_name,
    points=models.Batch(
        vectors=df_anime["vector_embeddings"],
        payloads=payloads,
        ids=df_anime.index
    )
)

client_connection.recommend(
    collection_name=qdrant_collection_name,
    positive=[1],
    negative=[0],
    score_threshold=0.1,
    limit=3
)