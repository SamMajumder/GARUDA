# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:30:55 2024

@author: Dr. M
"""

import streamlit as st

def about_page():
    st.title('About This App')
    
    st.image("https://raw.githubusercontent.com/SamMajumder/GARUDA/main/Streamlit-app-code/GARUDA-concept-art.webp", caption='Concept Art of GARUDA Interface')
    
    st.write("""
    ## What is this app?
    **G**uided **A**nalysis and **R**etrieval for **U**ser-**D**riven **D**ata **A**ssessment in spotify audio features is an application designed to provide comprehensive analysis and retrieval of Spotify audio features from Spotify's extensive music library. Leveraging Spotify's robust Web API, GARUDA allows users to compare Spotify audio features of a selected song with those of various songs in a playlist, delivering insights through visually engaging and interactive plots.

    ## Who built this app?
    Developed by Dr. Sambadi Majumder, a dedicated data scientist with a strong passion for exploring the intersection of music technology and advanced analytics. Sambadi Majumder's work focuses on leveraging machine learning techniques to unravel the complexities of music data, offering novel insights and tools to music enthusiasts and professionals alike.
    
    ## How to use this app?
    - **Compare Playlist**: Navigate to the 'Compare Playlist' page where you can select a Spotify playlist and analyze it against a track of your choice, seeing side-by-side comparisons of their musical features.
    - **Compare Genre**: Access the 'Compare Genre' page to delve into specific music genres, comparing songs within that genre to discover common attributes and variances.

    ## Source Code
    Interested in the source code? Visit the [GitHub repository](https://github.com/SamMajumder/GARUDA).

    ## Contact Information
    For more information, suggestions, or potential collaborations, feel free to drop an email at [sambadimajumder@gmail.com](mailto:sambadimajumder@gmail.com).

    ## Acknowledgements
    This work would not have been possible without **Spotify's Web API** and the incredible **Spotipy Python Module**

    - **Spotify's Web API**: This application makes extensive use of Spotify's Web API, which provides comprehensive data and robust functionalities for accessing and retrieving detailed Spotify audio information.
    - **Spotipy Python Module**: GARUDA utilizes the Spotipy module, a lightweight Python library that simplifies the process of accessing Spotify's Web API, allowing for straightforward authentication and data retrieval.

    """)


