# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:24:46 2024

@author: Dr. M
"""

import spotipy
from umap import UMAP
from sklearn.preprocessing import StandardScaler
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
from scipy.spatial.distance import euclidean
import plotly.express as px 
from dotenv import load_dotenv
import os

load_dotenv()



# Load environment variables
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, 
                                                      client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#####
### let's write a function that returns query results based on the keyword of a genre and page number specifications


def genre_keyword_search(genre_keyword, page_number):
    query_results = []
    
    ## this step is retrieving the information as a list of dictionaries 
    ## this retrieval is based on the genre_keyword and page number parameters
    ## each element in this list is a track
    for current_page in range(page_number):
        actual_offset = current_page * 50  # Calculate the actual offset to feed to the function
        results = sp.search(
            q=f'genre:{genre_keyword}',  # Ensure the query format is correct
            limit=50,
            type='track',
            offset=actual_offset
        )
        query_results.extend(results['tracks']['items'])
        print(f"Fetched {len(results['tracks']['items'])} items at offset {actual_offset}") 
        

    return query_results       

#### Get the track_id, album name and artist names for the tracks returned
## each element in the list is a dictionary which represents a track

## and then use the track id to get audio features for each 

## lets write a function that does this for us 

## one of the inputs is the query result from the genre_keyword_search

def get_audio_features(query): 
    
    ### Initialize a list 
    track_details = [] 
    
    ## getting the album names, artist names and track id 
    for tracks in query:
        id = tracks.get('id', 'unknown')
        album_names = tracks.get('album', {}).get('name', "unknown")
        artist_names = tracks.get('artists', [{}])[0].get('name', 'unknown')
        
        track_details.append({
            'Album_Name': album_names,
            'Artist_Name': artist_names,
            "id": id
        }) 
        
    ## convert the dictionary to a pandas dataframe 
    track_details_df = pd.DataFrame(track_details)
    
    ## now let's get the track id and convert it to the list
    # extracting the track ids 
    track_details_df_id = track_details_df['id'].tolist() 
    
    ######
    ## Now we can the audio features for each track
    ##### 
    
    ## Initialize a  list 
    ### now extracting the audio features for each track 

    ### initializing an empty list to hold the features 
    all_audio_features = []

    ## so the function sp.audio_features has a limit of 100 tracks at a time, 
    ## best way to get around this is process the thing in batches of 100

    ## here the range function starts from 0 and processes upto the length of the id list
    ## in batches/steps of 100  

    for i in range(0, len(track_details_df_id),100):
        ## first create the batch
        batch = track_details_df_id[i:i+100]
        audio_features = sp.audio_features(batch)
        all_audio_features.append(audio_features) 
        
        
    ### now let's write a loop where it iterates over each element all_audio_features and converts it to pandas dataframe

    ## intialize an empty pandas dataframe 
    audio_features_df = pd.DataFrame()

    for batch in all_audio_features:
        df = pd.DataFrame(batch)
        audio_features_df = pd.concat([audio_features_df,
                                       df],ignore_index=True)


    #### now inner-joining the audio features df to the track details df

    audio_features_df = pd.merge(audio_features_df,
                                 track_details_df,
                                 how = 'inner') 
    
    
    ## making a list of columns that we don't need 
    columns_to_drop = ['key','mode','type','uri','track_href','analysis_url',
                       'time_signature']


    audio_features_df.drop(columns = columns_to_drop,
                           inplace =True) 
    
    
    return audio_features_df

### performs a search based on an artist, song and album name and then extracts audio features from that
def user_song_info_and_audio_features(track_name, artist_name=None, album_name=None):
    
    
    # Build the search query based on provided inputs
    query = f"track:{track_name}"
    if artist_name:
        query += f" artist:{artist_name}"
    if album_name:
        query += f" album:{album_name}"
    
    # Conduct the search
    results = sp.search(q=query, type='track', limit=1)
    
    # Check if any tracks were found
    if not results['tracks']['items']:
        return pd.DataFrame()  # Return an empty DataFrame if no tracks found
    
    ### extracting id, album name and artist name and created a dataframe 

    # Extract the relevant information from the first track
    song_info = results['tracks']['items'][0]
    user_song_info = [{
        "id": song_info.get("id", "unknown"),
        "Artist_Name": ", ".join([artist['name'] for artist in song_info.get("artists", []) if 'name' in artist]),
        "Album_Name": song_info.get("album", {}).get("name", "unknown")
    }]

    # Convert list to DataFrame
    user_song_info_df = pd.DataFrame(user_song_info)

    # Get the audio features for the song
    user_song_audio_features = sp.audio_features(user_song_info_df['id'].tolist())

    # Convert audio features to DataFrame
    user_song_audio_features_df = pd.DataFrame(user_song_audio_features)

    # Inner-join the audio features DataFrame with the track details DataFrame
    final_df = pd.merge(user_song_audio_features_df, user_song_info_df, how='inner', on='id')

    # Columns to drop
    columns_to_drop = ['type', 'uri', 'track_href', 'analysis_url', 'time_signature', 'mode', 'key']
    final_df.drop(columns=[col for col in columns_to_drop if col in final_df.columns], inplace=True)

    
    
    return final_df

### perform umap and return dataframe with the umap results appended to the main table
def apply_umap(dataset, features, n_components=2, random_state=42):
    # Standardize the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(dataset[features])
    
    # Apply UMAP with a set random state for reproducibility
    umap_model = UMAP(n_components=n_components, random_state=random_state)
    umap_components = umap_model.fit_transform(scaled_features)
    
    # Create a new DataFrame with UMAP components
    umap_df = pd.DataFrame(umap_components, columns=[f'UMAP{i+1}' for i in range(n_components)])
    
    # Add labels to the DataFrame
    labels = dataset.drop(columns=features).reset_index(drop=True)
    umap_df = pd.concat([labels, umap_df], axis=1)
    
    return umap_df



### Writing a function that that will extract information from all the songs in the playlist 
## and return a pandas dataframe 

def extract_spotify_playlist_info(playlist_creator_name, playlist_id):
    # Initialize an empty list to store the 'items' aspect of all tracks
    all_track_items = []

    # Set the initial offset to be 0
    offset = 0

    # Loop to fetch tracks in batches of 100
    while True:
        # Fetch a batch of tracks
        response = sp.user_playlist_tracks(user=playlist_creator_name, 
                                           playlist_id=playlist_id, 
                                           offset=offset)
        
        # Add the fetched tracks to the all_track_items list
        all_track_items.extend(response['items'])
        
        # Check if there are more tracks to fetch; if not then break out of the loop
        if response['next'] is None:
            break
        
        # Update the offset for the next batch
        offset += len(response['items'])

    # Initialize the dictionary to hold all the values from the playlist
    alltracks_info = {}

    # Loop through each track and extract info for each song
    for track in all_track_items:
        # Get metadata for each track
        track_id = track["track"]["id"]  # This grabs track id
        artist_name = track["track"]["album"]["artists"][0]["name"]  # This grabs the artist name
        ## learned this from here: https://stackoverflow.com/questions/61624487/extract-artist-genre-and-song-release-date-using-spotipy
        external_artist_url = track["track"]["album"]["artists"][0]["external_urls"]["spotify"]
        album_name = track["track"]["album"]["name"]  # This grabs the album name
        track_name = track["track"]["name"]  # This grabs the track name

        # Store the information in the dictionary under the track id key
        alltracks_info[track_id] = {
            'Artist_Name': artist_name,
            'Album_Name': album_name,
            'track_name': track_name,
            'id': track_id,
            'external_artist_url': external_artist_url
        }

    # Convert the alltracks_info dictionary to a list of dictionaries
    data = list(alltracks_info.values())

    # Convert this list to a pandas dataframe
    df = pd.DataFrame(data)

    return df 


## a function that extracts the audio features from track ids of a playlist

def extract_spotify_playlist_audio_features(track_ids): 
    
    ## Initialize an empty list to store all the audio information for all tracks
    
    all_audio_features = [] 
    
    # Loop through the track IDs in batches of 100
    for i in range(0, len(track_ids), 100):
        # Fetch audio features for the current batch of track IDs
        batch = track_ids[i:i+100]
        audio_features = sp.audio_features(batch)
        
        # Add the fetched audio features to the all_audio_features list
        all_audio_features.extend(audio_features) 
        
        
    # Convert the list of audio features to a DataFrame
    audio_features_df = pd.DataFrame(all_audio_features) 
    
    ## making a list of columns that we don't need 
    columns_to_drop = ['key','mode','type','uri','track_href','analysis_url',
                       'time_signature'] 
    
    audio_features_df.drop(columns = columns_to_drop,
                           inplace =True) 
    
    
    return (audio_features_df)

