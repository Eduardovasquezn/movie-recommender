# Recommendation System: Content-Based Filtering

Welcome to the AI Recommendation System project! This repository contains the code and resources needed to run the recommendation system, demonstrated on my [YouTube video](https://youtu.be/KZq6J11Lq7Y).

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
    git clone https://github.com/Eduardovasquezn/movie-recommender.git
    cd movie-recommender
    ```

2. Navigate to the project directory:
    ```bash
    cd movie-recommender
    ```
    
3. Create and activate virtual environment:
    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```
    
4. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Set up the environment variables. Create a `.env` file using `.env-example` as a template:
    ```bash
    cp .env-example .env
     ```
2. Insert embeddings into the Qdrant database:
    ```bash
    python src/insert_collection_qdrant.py
    ```

3. Start the Streamlit app:
    ```bash
    streamlit run src/app.py
    ```
### Learn More
 
Don't forget to check out the video, like, comment, and subscribe for more advanced tutorials!

If you found the content helpful, consider subscribing to my 
[YouTube channel](https://www.youtube.com/channel/UCYZ_si4TG801SAuLrNl-v-g?sub_confirmation=1) to support me.


