import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Group 6")


# Create three columns 
col1, col2, col3 = st.columns([1,1,1])


# inside of the first column
with col1:
    st.image('images/everynoise.png')
    st.write('<a href="/songs"> Everynoise Spotify data</a>', unsafe_allow_html=True)
    
with col2:
    st.image('images/df.png')
    st.write('<a href="/dataframe"> Dataframe</a>', unsafe_allow_html=True)





