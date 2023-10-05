import pandas as pd
import streamlit as st
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random as rn
import seaborn as sns
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from collections import Counter
from PIL import Image
from streamlit_elements import elements, mui, html
pd.options.display.max_rows = None
#import opendatasets as od


st.set_page_config(layout="wide")
st.header("Steam Dashboard")
#Name,Id,Artists,Artists_Id,Release,Duration,Genre,
#Danceability,Energy,Key,Loudness,Speechiness,Acousticness,
#Instrumentalness,Liveness,Valeance,Tempo


@st.cache_data
def load_steam_data(fp, sample_percentage=100):
    print('Running load_steam_data...')

    # Read in a sample of the CSV file based on the sample_percentage
    df = pd.read_csv(fp, skiprows=lambda x: x % (100 // sample_percentage) != 0)

    return df

sample_percentage = 20  # Change this to your desired percentage

# Loading the data
fp1 = './data/dataset.csv'
df1 = load_steam_data(fp1, sample_percentage)
df1 = df1.drop(df1[df1.review_text == 'Early Access Review'].index)

fp2 = './data/steam.csv'
df2 = load_steam_data(fp2)

split_genres = df2["genres"].str.split(";", n=1, expand=True)
df2["genres"] = split_genres[0]
game_genres = df2["genres"].value_counts()[:15]

selected_genre = st.sidebar.selectbox("Select Genre:", game_genres.index)

col1, col2 = st.columns( [4,4] )

with col1:
    st.write('Genre Graph')
    # create a list of all the state names
    game_genres.plot(kind="barh", color='#005f8b')
    plt.gca().invert_yaxis()

    plt.xlabel('Amount of Games in Category')
    plt.ylabel('Category')
    plt.title('Top 15 Categoires with the Most Games')

    sns.set(rc={'figure.figsize':(10,8)})

    st.pyplot(plt.gcf())


with col2:
    st.write(f'{selected_genre} Genre Descriptions')
    combined_df = pd.merge(df1, df2, left_on='app_id', right_on='appid', how='left')
    combined_df.review_text = combined_df.review_text.astype('str')
    genre_df = combined_df[combined_df['genres'] == selected_genre]
    txt = ' '.join(rev for rev in genre_df.review_text)
    plt.figure(figsize=(15,8))

    wordcloud = WordCloud(
            background_color = 'black',
            max_font_size = 100,
            max_words = 100,
            width = 1000,
            height = 600
            ).generate(txt)


    plt.imshow(wordcloud,interpolation = 'bilinear')
    plt.axis('off')
    st.pyplot(plt.gcf())