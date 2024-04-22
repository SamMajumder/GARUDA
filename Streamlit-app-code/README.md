# Streamlit Application Code for GARUDA Project

## Introduction
This directory contains the Streamlit application code for the GARUDA project, which is designed to provide an interactive web interface for comparing music data. The scripts here handle the web interface components and the interactivity elements of the application.

## Dependencies
- `streamlit`: Used to create and manage the web app.
- `streamlit_option_menu`: An extension for Streamlit that allows adding option menus.
- `plotly.express`: For creating interactive plots and visualizations.
- `pandas`: For data manipulation and analysis.
- `spotipy`: A lightweight Python library for the Spotify Web API, used for accessing Spotify's data.
- `scikit-learn`: For implementing machine learning algorithms including `StandardScaler`.
- `umap-learn`: For dimensionality reduction using Uniform Manifold Approximation and Projection.
- `python-dotenv`: For loading environment variables from a `.env` file, ensuring sensitive keys are kept secret.
- `os`: For interacting with the operating system, used to manage environment variables and file paths.


## File Descriptions
- `about_page.py`: Provides an "About" page within the Streamlit app.
- `Multipage.py`: Handles the logic for managing multiple pages in the Streamlit app.
- `streamlit_compare_genre_page.py`: Streamlit page for comparing different music genres.
- `streamlit_compare_playlist_page.py`: Streamlit page for comparing user-selected playlists.
- `utils.py`: Contains utility functions used across various pages of the Streamlit app.

## Contact Information
For further inquiries or support, please contact Dr. Sambadi Majumder at sambadimajumder@gmail.com

## Credits and Acknowledgments
Special thanks to the contributors of the open-source libraries used in this project, such as **Streamlit**, **Plotly**, **Pandas**, **Spotipy**, **Scikit-learn**, and **UMAP-learn**, which have significantly enhanced the development of this interactive application.
