# G.A.R.U.D.A. :

![Concept Image](https://raw.githubusercontent.com/SamMajumder/GARUDA/main/Streamlit-app-code/GARUDA-concept-art.webp)

<p align="center">
  <img src="https://raw.githubusercontent.com/SamMajumder/GARUDA/main/Streamlit-app-code/GARUDA-concept-art.webp" alt="Concept Image">
  <br>
  Created using DALL-E by OpenAI
</p>


## Overview
 **G**uided **A**nalysis and **R**etrieval for **U**ser-**D**riven **D**ata **A**ssessment in spotify audio features is an application designed to provide comprehensive analysis and retrieval of Spotify audio features from Spotify's extensive music library. Leveraging Spotify's robust Web API, GARUDA allows users to compare Spotify audio features of a selected song with those of various songs in a playlist, delivering insights through visually engaging and interactive plots.

[Check out the GARUDA app here](https://garuda.streamlit.app/)

## Background
The name **GARUDA** is inspired by the mythical bird-like creature known in Hindu mythology as the king of birds and the vahana (mount) of Lord Vishnu. Known for its speed, strength, and martial prowess, Garuda represents the ability to swiftly navigate vast spaces and carry immense wisdom. This mirrors the application’s capability to efficiently handle and analyze vast amounts of musical data, providing quick and insightful results to its users.

## Features
**GARUDA** offers two powerful features to explore and analyze Spotify audio features:

### Playlist Comparison Tool
- **Song Comparison**: Compare the Spotify audio features of any selected song against a range of songs from a specified Spotify playlist.
- **Interactive Visualizations**: Utilizes advanced data visualization techniques to present the similarity and differences between the user's song and playlist songs.

### Genre Analysis Tool
- **Genre-Based Search**: Allows users to input a genre keyword to fetch related tracks from Spotify, enhancing the scope of comparison.
- **Detailed Search Options**: Users can specify artist, album, and track details to refine their search.
- **Comparative Analysis**: Compares the audio features of the user's specified song with those from the genre-based search results.

## How It Works
**GARUDA** operates through a straightforward user-driven process:

### Playlist Comparison Tool
1. **User Input**: Users input the name of an artist, song, and a Spotify playlist ID.                                                                                                                                      **Note**: This is how you retrieve the playlist id from a spotify playlist link ## Playlist ID Visualization

![Playlist ID](https://raw.githubusercontent.com/SamMajumder/GARUDA/main/playlist_id.png)


2. **Data Retrieval**: Retrieves the Spotify audio features of the specified song and all songs within the provided playlist using Spotify's Web API.
3. **Analysis and Comparison**: Analyzes and compares these features, highlighting how similar or different the selected song is from those in the playlist.
4. **Visualization**: Displays results through interactive UMAP plots that map out the similarity landscape, making it easy to visualize the comparative analysis.

### Genre Analysis Tool
1. **Genre Keyword Input**: Users enter a genre keyword and specify the number of pages to fetch, initiating a genre-specific search.
2. **User Song Details**: Users provide details about an artist, album, and track for which they seek a comparison.
3. **Fetch and Compare**: Retrieves songs related to the specified genre and compares their Spotify audio features with the user's song, displaying the results in an interactive format.

## Use Cases
**GARUDA** serves a diverse range of users, providing in-depth musical analysis and comparison through its dual-feature design:

### Playlist Comparison Tool
- **Music Enthusiasts**: Discover how your favorite song compares to others in different playlists based on various Spotify audio attributes.
- **Artists and Producers**: Gain insights into the Spotify audio features that distinguish your work from others, potentially guiding future music production decisions.
- **Researchers and Academics**: Analyze trends and patterns in Spotify audio features across different genres or artist repertoires to conduct musicology research.

### Genre Analysis Tool
- **Genre Explorers**: Users can explore how songs within a specific genre compare to a chosen track, providing a deeper understanding of genre characteristics.
- **Playlist Curators**: Enhance playlist creation by identifying songs that match or diversify the audio profile of existing playlists based on detailed genre-specific searches.
- **Music Marketers and Analysts**: Utilize detailed genre analysis to understand market trends, helping tailor marketing strategies to audience preferences based on audio feature analysis.


## Acknowledgments
This work would not have been possible without **Spotify's Web API** and the incredible **Spotipy Python Module**

- **Spotify's Web API**: This application makes extensive use of Spotify's Web API, which provides comprehensive data and robust functionalities for accessing and retrieving detailed Spotify audio information.
- **Spotipy Python Module**: GARUDA utilizes the Spotipy module, a lightweight Python library that simplifies the process of accessing Spotify's Web API, allowing for straightforward authentication and data retrieval.
