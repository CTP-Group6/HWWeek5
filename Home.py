import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Welcome!"
)

# Create a page header
st.header("Group 6")


# Create three columns 
col1, col2, col3, col4 = st.columns([1,1,1,1])


# inside of the first column
with col1:
    st.image('images/everynoise.png')
    st.write('<a href="/songs"> Everynoise Spotify data</a>', unsafe_allow_html=True)
    
with col2:
    st.image('images/df.png')
    st.write('<a href="/dataframe"> Dataframe</a>', unsafe_allow_html=True)

with col3:
    st.image('images/steam.png')
    st.write('<a href="/steam"> Steam</a>', unsafe_allow_html=True)

with col4:
    st.image('images/steamplayersss.png')
    st.write('<a href="/steamplayers"> SteamPlayers</a>', unsafe_allow_html=True)

