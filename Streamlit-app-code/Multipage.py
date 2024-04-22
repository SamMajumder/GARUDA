# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:54:29 2024

@author: Dr. M
"""

import streamlit as st
from streamlit_option_menu import option_menu
from utils import * ## may not be required but doing it just to be sure that we are importing the client id and client secret

# Import page functions
from streamlit_compare_playlist_page import compare_playlist_page
from streamlit_compare_genre_page import compare_genre_page
from about_page import *

def main():
    st.title('GARUDA')
    # Sidebar navigation
    #st.sidebar.title('Navigation')
    selected = option_menu("Menu", ["About", "Compare Genre", "Compare Playlist"],
                           icons=['info-circle', 'music-note-beamed', 'music-note-list'],
                           menu_icon="cast", default_index=0)

    if selected == "About":
        about_page()
    elif selected == "Compare Genre":
        compare_genre_page()
    elif selected == "Compare Playlist":
        compare_playlist_page()

if __name__ == "__main__":
    main()