# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:29:32 2024

@author: Dr. M
"""

from utils import *


def main():
    
    ## retrieve information about the genre progressive metal for upto 4 pages
    query = genre_keyword_search(genre_keyword = "progressive metal", 
                                      page_number = 4)   
    
    ##### now let's get audio features for each track 
    audio_features_df = get_audio_features(query) 


    #### Now we will do the same for a track chosen by the user 
    user_song_info_df = user_song_info_and_audio_features(artist_name = "Vitalism",
                                                          album_name = "Gradus", 
                                                          track_name = "Gradus")   
        
    
    ### Now we can compare between user_song_info_df and audio_features_df 

    ## Step 1
    ## First we need to add a column to each dataframe which clearly signifies the source of the songs
    user_song_info_df["Source"] = "user"

    audio_features_df["Source"] = "searched"
    ## Second we concatenate the two dataframes 

    ### now we can compare the two using UMAP 
    ## step 2 create a combined dataset 
    df = pd.concat([audio_features_df, user_song_info_df], ignore_index=True)

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

    fig_umap_playlist.write_html('umap_searched_versus_user.html')


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
    

    
if __name__ == '__main__':
    main()











