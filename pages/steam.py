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
pd.options.display.max_rows = None
#import opendatasets as od


st.set_page_config(layout="wide")
st.header("Steam Dashboard")
#Name,Id,Artists,Artists_Id,Release,Duration,Genre,
#Danceability,Energy,Key,Loudness,Speechiness,Acousticness,
#Instrumentalness,Liveness,Valeance,Tempo


@st.cache_data
def load_steam_data(fp):
    print('Running load_steam_data...')

    # read in the csv via the link
    df = pd.read_csv(fp)

    return(df)


# loading the data
fp1 = './data/dataset.csv'
df1 = load_steam_data(fp1)

fp2 = './data/steam.csv'
df2 = load_steam_data(fp2)

split_genres = df2["genres"].str.split(";", n=1, expand=True)
df2["genres"] = split_genres[0]
game_genres = df2["genres"].value_counts()[:15]

col1, col2 = st.columns( [4,4] )

with col1:
    st.write('Genre Graph')
    # create a list of all the state names
    game_genres.plot(kind="barh")
    plt.gca().invert_yaxis()

    plt.xlabel('Amount of Games in Category')
    plt.ylabel('Category')
    plt.title('Top 15 Categoires with the Most Games')

    sns.set(rc={'figure.figsize':(10,8)})

    st.pyplot(plt.gcf())


with col2:
    st.write('RPG Genre Descriptions')
    combined_df = pd.merge(df1, df2, left_on='app_id', right_on='appid', how='left')
    combined_df.review_text = combined_df.review_text.astype('str')
    rpg_df = combined_df[combined_df['genres'] == 'RPG']
    txt = ' '.join(rev for rev in rpg_df.review_text)
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