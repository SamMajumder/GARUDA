# Base-Code for GARUDA Project

## Introduction
This directory contains essential scripts for analyzing and comparing music data using the Spotify API. It includes utilities for genre comparison and playlist comparison, which form the core analytical capabilities of the GARUDA project.

## Dependencies
- `spotipy`: A lightweight Python library for the Spotify Web API.
- `pandas`: For data manipulation and analysis.
- `scikit-learn`: For machine learning tools and statistical modeling, particularly the `StandardScaler` for data normalization.
- `umap-learn`: For dimensionality reduction using Uniform Manifold Approximation and Projection.
- `plotly.express`: For creating interactive plots and visualizations.
- `python-dotenv`: For loading environment variables from a `.env` file, ensuring sensitive keys are kept secret.

## File Descriptions
- `base_code_compare_genre.py`: Analyzes and compares different music genres based on their audio features.
- `base_code_compare_playlist.py`: Compares playlists to find similarities and differences in their musical compositions.

## Contact Information
For further inquiries or support, please contact Dr. Sambadi Majumder at sambadimajumder@gmail.com

## Credits and Acknowledgments
This project utilizes several open-source packages, including **Spotipy**, **Pandas**, **Scikit-learn**, **UMAP-learn**, **Plotly**, and **Python-dotenv**, which greatly simplified the API interactions and data handling.
