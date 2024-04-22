# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:48:12 2024

@author: samba
"""

from utils import *

#### Initialize the playlist creator's name and the playlist id 

playlist_creator_name = "aaronflem"
playlist_id = "6gKFBSRW6idivPSA6cMlZV" 


def main():
    
    ## extracting information about every song in the playlist 

    playlist_info = extract_spotify_playlist_info(playlist_creator_name = playlist_creator_name, 
                                              playlist_id = playlist_id)


    ## isolating the track ids
    track_ids = playlist_info['id'].tolist()

    ## getting the audio features into a dataframe 
    playlist_audio_features = extract_spotify_playlist_audio_features(track_ids=track_ids)

    ### Now we need to join playlist_audio_features with playlist_info
    playlist_audio_features = pd.merge(playlist_info,playlist_audio_features)



    #### Now we will do the same for a track chosen by the user 
    user_song_info_df = user_song_info_and_audio_features(artist_name = "Vitalism",
                                                          album_name = "Gradus", 
                                                          track_name = "Gradus")   


    ### Now we can compare between user_song_info_df and playlist_audio_features

    ## Step 1
    ## First we need to add a column to each dataframe which clearly signifies the source of the songs
    user_song_info_df["Source"] = "user"

    playlist_audio_features["Source"] = "playlist"
    ## Second we concatenate the two dataframes 

    ### now we can compare the two using UMAP 
    ## step 2 create a combined dataset 
    df = pd.concat([playlist_audio_features, user_song_info_df], ignore_index=True)

    ## step 3 define which columns we want to use to create a UMAP 
    ## columns to be used for UMAP 
    features = ['danceability', 'energy', 'loudness', 'speechiness', 
                'acousticness','instrumentalness', 'liveness', 'valence', 
                'tempo','duration_ms'] 



    ### step 4 perform UMAP  
    umap_result = apply_umap(df, features = features, n_components=2,
                             random_state=123)


    ## Step 5 
    ### Visualize the umap as scatter plots##
    # UMAP plot for the playlist dataset
    fig_umap_playlist = px.scatter(umap_result, 
                                   x='UMAP1', 
                                   y='UMAP2', 
                                   color='Source',
                                   hover_data=['Album_Name', 
                                               'Artist_Name'],
                                   title='Searched vs User: UMAP')

    fig_umap_playlist.write_html('umap_playlist_versus_user.html')


    ######
    ## Next we calculate the Euclidean distances 

    ## Step 1 is to create two separate dataframes
    ## one for searched songs 
    playlist_umap = umap_result[umap_result["Source"] == "playlist"]
    user_umap = umap_result[umap_result["Source"] == "user"]

    # Calculate Euclidean distance
    ##playlist
    playlist_umap['Euclidean_Distance'] = playlist_umap.apply(
        lambda row: euclidean(row[['UMAP1','UMAP2']], user_umap[['UMAP1','UMAP2']].iloc[0]), axis=1) 


    #### Now sorting the dataframe based on the Euclidean distance values 
    playlist_umap = playlist_umap.sort_values(by = 'Euclidean_Distance',
                                              ascending = True) 

     
    
if __name__ == '__main__':
    main()

