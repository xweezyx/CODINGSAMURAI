import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=eaac40a8f88e04d4025dc11ff3c31fdb&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox('Enter the name of a movie', movies['title'].values)

if st.button('Recommend'):
    movie_names, posters = recommend(selected_movie_name)

    pic1, pic2, pic3, pic4, pic5 = st.columns(5)
    with pic1:
        st.text(movie_names[0])
        st.image(posters[0])
    with pic2:
        st.text(movie_names[1])
        st.image(posters[1])
    with pic3:
        st.text(movie_names[2])
        st.image(posters[2])
    with pic4:
        st.text(movie_names[3])
        st.image(posters[3])
    with pic5:
        st.text(movie_names[4])
        st.image(posters[4])
