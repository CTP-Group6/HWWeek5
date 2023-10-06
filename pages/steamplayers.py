import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import plotly.express as px

df = pd.read_csv("data/steam_merge.csv")

split_genres = df['genres'].str.split(';',n = 1, expand=True)
df["genres"] = split_genres[0]
genre_values = df['genres'].unique()
#np.insert(df['genres'].unique(),0,values="All")
month_values = np.insert(df['Month'].unique(),0,values="All")
grouped_df = df.groupby(['genres', 'Game'])['Avg. Players'].mean().reset_index()

unique_genres = df['genres'].unique()


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state='auto'
)


# Create a page header
st.title("Group 6") # H1 tag

def create_chart(df,genre,timeframe):
    fig, ax = plt.subplots(figsize=(13,8))
    genre_data = grouped_df[grouped_df['genres'] == genre]
    if(genre == 'Action'):
        fig = px.scatter(genre_data, x='Avg. Players', y='Game', color='Avg. Players', hover_name = 'Game')
        fig.update_traces(hoverinfo='x+y')
        fig.update_layout(
            xaxis_title='Average Player Count',
            yaxis_title='Game Title',
            title=f'Average Player Count for {genre} Games',
            template='plotly_white'
        )
        st.plotly_chart(fig)
    else:
        plt.barh(genre_data['Game'], genre_data['Avg. Players'], color='skyblue')
        plt.gca().invert_yaxis()
        plt.yticks(rotation=45)
        plt.xlabel('Average Player Count')
        plt.ylabel('Game Title')
        plt.title(f'Average Player Count for {genre} Games')
        st.pyplot(plt)
    




with st.sidebar: # creates side bar
    genre = st.selectbox(
        label = "Select Genre Below",
        options = genre_values
    )
    timeframe = st.select_slider(
        "Select a Timeframe", 
        options = np.flip(month_values), 
        value = ('January 2020', 'August 2016')
        )
   
create_chart(df, genre, timeframe)