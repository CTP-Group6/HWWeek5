import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


st.set_page_config(layout="wide")
st.header("Everynoise Dashboard")
#Name,Id,Artists,Artists_Id,Release,Duration,Genre,
#Danceability,Energy,Key,Loudness,Speechiness,Acousticness,
#Instrumentalness,Liveness,Valeance,Tempo


@st.cache_data
def load_song_data(fp):
    print('Running load_song_data...')

    # read in the csv via the link
    df = pd.read_csv(fp)

    return(df)


# loading the data
fp = './data/songs.csv'
df = load_song_data(fp) 

col1, col2 = st.columns( [1,4] )

with col1:
    #st.write('Temp')
    # create a list of all the state names
    genre_list = sorted(df['Genre'].unique())
    
    # create a mulit select button
    #selected_genres = st.multiselect(
       # 'Select which genres to compare.',
       # genre_list
        #)


    # for debugging
    print(type(selected_genres), selected_genres)


    # extract just the selected genres
    #genre_df = df[df['Genre'].isin(selected_genres)].copy()


with col2:
    st.write("Dancability and Duration")
    st.write("Generally, Danceability decreases as Duration increases")
    
    correlation = df['Danceability'].corr(df['Duration'])
    plt.figure(figsize=(16, 14))
    sns.scatterplot(x='Duration', y='Danceability', data=df)
    sns.regplot(x='Duration', y='Danceability', data=df, scatter=False, color='red')
    plt.xlabel('Duration (ms)') 
    plt.ylabel('Danceability')
    plt.xlim(100000, 1500000)
    plt.ylim(0.00, 1.00)
    x_ticks = np.arange(100000, 1500000, 100000)
    plt.xticks(x_ticks)
    st.pyplot(plt.gcf())
