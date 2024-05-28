import os

import pandas as pd
import qdrant_client
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

qdrant_host = os.getenv("QDRANT_HOST")
qdrant_collection_name = os.getenv("QDRANT_COLLECTION_NAME")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

@st.cache_data
def load_datasets():
    df_anime = pd.read_csv('./data/df_anime_sample.csv')
    df_users_with_rating = pd.read_csv('./data/df_users_with_ratings_sample.csv')
    return df_anime, df_users_with_rating


def generate_recommendations(df_user, user_id, df_anime_ratings, k):
    client = qdrant_client.QdrantClient(
        qdrant_host,
        api_key=qdrant_api_key,
        timeout=50
    )

    # df_users_with_ratings
    filtered_user = df_user[df_user['user_id'] == user_id]

    anime_id_high_rating = filtered_user[filtered_user['rating'] > 5]['anime_id'].tolist()
    anime_id_low_rating = filtered_user[filtered_user['rating'] < 5]['anime_id'].tolist()

    high_rating = df_anime_ratings[df_anime_ratings['MAL_ID'].isin(anime_id_high_rating)].index
    low_rating = df_anime_ratings[df_anime_ratings['MAL_ID'].isin(anime_id_low_rating)].index

    # Approximate Nearest Neighbors. Semantic Search
    k_recommendations = client.recommend(
        collection_name=qdrant_collection_name,
        positive=high_rating,
        negative=low_rating,
        score_threshold=0.01,
        limit=k,
    )
    # Sort the list based on the 'score' attribute
    sorted_scored_points = sorted(k_recommendations, key=lambda x: x.score, reverse=True)

    # Extract titles and other attributes using list comprehension
    titles = [{
        'name': scored_point.payload['Name'],
        'japanese_name': scored_point.payload['Japanese name'],
        'score': scored_point.payload['Score'],
        'genres': scored_point.payload['Genres'],
        'poster_url': scored_point.payload['poster_url']
    } for scored_point in sorted_scored_points]

    return titles
