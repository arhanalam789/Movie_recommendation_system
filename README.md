# Movie Recommendation System

This project is a content-based movie recommendation system. The model has been trained, and its components are serialized for quick inference.

## Project Files
- **`movies_metadata.csv`**: The dataset containing metadata about the movies used for training.
- **`df.pkl`**: A serialized pandas DataFrame containing the preprocessed movie data.
- **`tfidf.pkl`**: The trained TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer used to extract features from movie text data (e.g., descriptions or overviews).
- **`tfidf_matrix.pkl`**: The transformed TF-IDF matrix representing the feature vectors of the movies.
- **`indices.pkl`**: A mapping of movie titles to their respective indices in the DataFrame to quickly look up movies during the recommendation process.

## How it Works
The recommendation engine uses TF-IDF to analyze the text data of movies. By computing the cosine similarity between the TF-IDF vectors of different movies, the system can recommend movies that are most similar to a given movie in terms of content.

## Status
The model is fully trained and properly serialized. All necessary objects have been saved as `.pkl` files, making it easy to build an API or a script to load these files and generate recommendations interactively.
