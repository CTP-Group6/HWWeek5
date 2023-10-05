import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache_data
def load_song_data(fp):
    print('Running load_song_data...')

    # read in the csv via the link
    df = pd.read_csv(fp)

    return(df)


# loading the data
fp = './data/songs.csv'
df = load_song_data(fp) 
df


