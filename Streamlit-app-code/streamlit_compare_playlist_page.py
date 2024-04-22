# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:58:34 2024

@author: Dr. M
"""


from utils import * 
import streamlit as st


def compare_playlist_page():
    st.title('Playlist Comparator')

    # User Inputs for playlist and song comparison
    st.subheader('Enter Playlist Details')
    playlist_creator_name = st.text_input('Playlist Creator’s Spotify Username:')
    playlist_id = st.text_input('Playlist ID:')

    st.subheader('Enter Song Details for Comparison')
    artist_name = st.text_input('Artist name:', 'Vitalism')
    album_name = st.text_input('Album name:', 'Gradus')
    track_name = st.text_input('Track name:', 'Gradus')

    # Button to trigger the analysis
    if st.button('Compare Song'):
        # Extracting information about every song in the playlist
        playlist_info = extract_spotify_playlist_info(playlist_creator_name=playlist_creator_name, 
                                                      playlist_id=playlist_id)

        # Isolating the track ids
        track_ids = playlist_info['id'].tolist()

        # Getting the audio features into a dataframe
        playlist_audio_features = extract_spotify_playlist_audio_features(track_ids=track_ids)
        playlist_audio_features = pd.merge(playlist_info, playlist_audio_features)

        # Information for a track chosen by the user
        user_song_info_df = user_song_info_and_audio_features(artist_name=artist_name,
                                                              album_name=album_name,
                                                              track_name=track_name)

        # Signifying the source of the songs
        user_song_info_df["Source"] = "user"
        playlist_audio_features["Source"] = "playlist"

        # Combine datasets for UMAP analysis
        combined_df = pd.concat([playlist_audio_features, user_song_info_df], ignore_index=True)

        # Perform UMAP
        features = ['danceability', 'energy', 'loudness', 'speechiness',
                    'acousticness', 'instrumentalness', 'liveness', 'valence',
                    'tempo', 'duration_ms']
        
        umap_result = apply_umap(combined_df, features=features, n_components=2, random_state=123)

        # Visualize UMAP
        fig_umap_playlist = px.scatter(umap_result, 
                                       x='UMAP1', 
                                       y='UMAP2', 
                                       color='Source',
                                       hover_data=['Album_Name', 'Artist_Name'],
                                       title='Playlist vs User: UMAP',
                                       color_discrete_map={'user': 'red', 
                                                           'playlist': 'blue'})
        
        st.plotly_chart(fig_umap_playlist, use_container_width=True)

        ######
        ## Next we calculate the Euclidean distances 

        ## Step 1 is to create two separate dataframes
        ## one for searched songs 
        
        # Calculate Euclidean distance
        playlist_umap = umap_result[umap_result["Source"] == "playlist"]
        
        user_umap = umap_result[umap_result["Source"] == "user"]
        
        # Calculate Euclidean distance
        playlist_umap['Euclidean_Distance'] = playlist_umap.apply(
            lambda row: euclidean(row[['UMAP1', 'UMAP2']], user_umap[['UMAP1', 'UMAP2']].iloc[0]), axis=1)

        # Sorting the dataframe by Euclidean distance
        playlist_umap_sorted = playlist_umap.sort_values(by='Euclidean_Distance', ascending=True)
        st.dataframe(playlist_umap_sorted)

