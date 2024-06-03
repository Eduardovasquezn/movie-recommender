# Recommendation System: Content-Based Filtering

This repository contains the code and resources needed to run the recommendation system, demonstrated on my [YouTube video](https://youtu.be/KZq6J11Lq7Y).

## Project Overview

This project is a content-based recommendation system built using Python. It consists of the following components:
- **Data Insertion**: Script to insert embeddings into the Qdrant vector store database (located in `src/insert_collection_qdrant.py`)
- **Utilities**: Functions used to build the recommender system (located in `src/utils.py`)
- **Frontend**: Developed using Streamlit (located in `src/app.py`)
- **Dataset**: The dataset used for the system (located in the `data` folder)
- **Requirements**: List of required libraries (located in `requirements.txt`)
- **Environment Variables**: Example file for necessary credentials (located in `.env.example`)

## Getting Started

### Installation

1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/Eduardovasquezn/movie-recommender.git)
    cd movie-recommender
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:
    - Copy the `.env.example` file to `.env`
    - Fill in your credentials in the `.env` file

### Running the Application

1. Insert embeddings into the Qdrant database:
    ```bash
    python src/insert_collection_qdrant.py
    ```

2. Start the Streamlit app:
    ```bash
    streamlit run src/app.py
    ```
### Learn More
 
Don't forget to check out the video, like, comment, and subscribe for more advanced tutorials!

If you found the content helpful, consider subscribing to my 
[YouTube channel](https://www.youtube.com/channel/UCYZ_si4TG801SAuLrNl-v-g?sub_confirmation=1) to support me.


