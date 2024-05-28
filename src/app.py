import streamlit as st

from utils import load_datasets, generate_recommendations

st.set_page_config(page_title="Anime Recommender", layout="wide", initial_sidebar_state="expanded")

df_anime, df_users_with_rating = load_datasets()

unique_user_id = df_users_with_rating['user_id'].unique().tolist()

def main():
    st.markdown('<h1 style="color: red;">AnimeStream - Anime Recommender⛩️</h1>', unsafe_allow_html=True)

    st.write("##")

    st.markdown("""
        <p>Welcome to <b style="color:#E50914;">AnimeStream</b>, your personalized anime recommendation system 
        tailored to your watch history!</p>
    """, unsafe_allow_html=True)

    st.write("##")

    my_expander = st.expander("Tap to Select a User ID 👤💻")

    selected_user_id = my_expander.selectbox('', unique_user_id)
    if my_expander.button("Recommend"):

        anime_info = generate_recommendations(df_user=df_users_with_rating,
                                              user_id=selected_user_id,
                                              df_anime_ratings=df_anime, k=5)

        # Displaying in Streamlit
        cols = st.columns(5)
        for anime, col in zip(anime_info, cols):
            print(f"Anime: {anime}")
            print(f"col: {col}")
            col.write(f'<b style="color:#E50914">English Name</b>:<b> {anime["name"]}</b>', unsafe_allow_html=True)
            col.write(f'<b style="color:#E50914">Japanese Name</b>:<b> {anime["japanese_name"]}</b>',
                      unsafe_allow_html=True)
            st.write("##")
            col.image(anime["poster_url"], use_column_width=True)
            st.write("##")
            col.write("________")
            # Assuming you have vote data available
            col.write(f'<b style="color:#DB4437">Rating</b>:<b> {anime["score"]}</b>', unsafe_allow_html=True)
            col.write(f'<b style="color:#DB4437">Genres</b>: <b> {anime["genres"]} <b> ', unsafe_allow_html=True)

if __name__ == "__main__":
    main()



