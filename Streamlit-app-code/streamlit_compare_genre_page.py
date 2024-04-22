# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:32:20 2024

@author: samba
"""

from utils import * 
import streamlit as st

def compare_genre_page():
    st.title('Genre Analysis Tool')

    # User Inputs
    st.subheader('Search by genre')
    genre_keyword = st.text_input('Enter genre keyword:', 'progressive metal')
    page_number = st.number_input('Number of pages to fetch:', min_value=1, value=4)

    # Adding a subheading before Artist Name input
    st.subheader('User Artist Details')  # or use st.markdown("### Artist Details") for smaller heading
    artist_name = st.text_input('Artist name:', '')
    album_name = st.text_input('Album name:', '')
    track_name = st.text_input('Track name:', '')

    # Button to perform search
    if st.button('Perform Search'):
        # Perform genre keyword search
        query_results = genre_keyword_search(genre_keyword, page_number)

        # Get audio features for the fetched tracks
        audio_features_df = get_audio_features(query_results)

        # Fetch user song info and audio features
        user_song_info_df = user_song_info_and_audio_features(artist_name=artist_name,
                                                              album_name=album_name, 
                                                              track_name=track_name)
        
        
        ### Now we can compare between user_song_info_df and audio_features_df 

        ## Step 1
        ## First we need to add a column to each dataframe which clearly signifies the source of the songs
        user_song_info_df["Source"] = "user"

        audio_features_df["Source"] = "searched"
        
        
        ### now we can compare the two using UMAP 
        ## step 2 create a combined dataset 
        # Combine datasets
        df = pd.concat([audio_features_df, user_song_info_df], ignore_index=True)
        
        ## columns to be used for UMAP 
        features = ['danceability', 'energy', 'loudness', 'speechiness', 
                    'acousticness','instrumentalness', 'liveness', 'valence', 
                    'tempo','duration_ms'] 

        # Apply UMAP
        umap_result = apply_umap(df, features=features, n_components=2, random_state=123)

        # Display UMAP plot
        fig_umap_playlist = px.scatter(umap_result, x='UMAP1', y='UMAP2', color='Source',
                                       hover_data=['Album_Name', 'Artist_Name'],
                                       title='Searched vs User: UMAP',
                                       color_discrete_map={'user': 'red', 
                                                           'searched': 'blue'})
        
        st.plotly_chart(fig_umap_playlist)

        # Display the searched umap DataFrame
        ######
        ## Next we calculate the Euclidean distances 

        ## Step 1 is to create two separate dataframes
        ## one for searched songs 
        searched_umap = umap_result[umap_result["Source"] == "searched"]
        user_umap = umap_result[umap_result["Source"] == "user"]
        
        # Calculate Euclidean distance
        ##playlist
        searched_umap['Euclidean_Distance'] = searched_umap.apply(
            lambda row: euclidean(row[['UMAP1','UMAP2']], user_umap[['UMAP1','UMAP2']].iloc[0]), axis=1) 
        
        
        #### Now sorting the dataframe based on the Euclidean distance values 
        searched_umap = searched_umap.sort_values(by = 'Euclidean_Distance',
                                                  ascending = True) 
        
        st.dataframe(searched_umap)

