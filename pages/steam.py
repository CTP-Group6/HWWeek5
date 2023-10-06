import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from streamlit_elements import nivo
from streamlit_elements import elements, mui, html
import plotly.express as px


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

fp2 = './data/steam.csv'
df2 = load_steam_data(fp2)

split_genres = df2["genres"].str.split(";", n=1, expand=True)
df2["genres"] = split_genres[0]
game_genres = df2["genres"].value_counts()[:10]

selected_genre = st.sidebar.selectbox("Select Genre:", game_genres.index)

col1, col2= st.columns( [4,4] )

with col1:
    st.write('### Genre Distribution')
    if selected_genre:
        # Prepare data for Plotly Bar Chart
        pie_data = game_genres.reset_index()
        pie_data.columns = ['Category', 'Count']

        # Create Plotly Bar Chart
        fig = px.bar(
            pie_data,
            x="Category",
            y="Count",
            labels={"Category": "Genre", "Count": "Number of games"},
            title="Genre Distribution",
        )
        st.plotly_chart(fig)


with col2:
    st.write(f'{selected_genre} Genre Descriptions')
    combined_df = pd.merge(df1, df2, left_on='app_id', right_on='appid', how='left')
    combined_df.review_text = combined_df.review_text.astype('str')
    combined_df['review_text'] = combined_df['review_text'].str.replace('Early Access Review', '', case=False)
    genre_df = combined_df[combined_df['genres'] == selected_genre]
    txt = ' '.join(rev for rev in genre_df.review_text)
    
    plt.figure(figsize=(15, 8))
    wordcloud = WordCloud(
        background_color='black',
        max_font_size=100,
        max_words=100,
        width=1000,
        height=600
    ).generate(txt)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt.gcf())



