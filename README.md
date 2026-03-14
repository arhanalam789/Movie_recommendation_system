<div align="center">
  <img src="https://img.icons8.com/nolan/256/movie-projector.png" width="100" />
  <h1>🎬 Movie Recommendation System</h1>
  <p><i>A smart, fast, and scalable content-based movie recommendation API built with FastAPI and TMDB</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
    <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  </p>
</div>

---

## 🚀 Overview

This project is a powerful **content-based movie recommendation API**. By leveraging advanced TF-IDF (Term Frequency-Inverse Document Frequency) algorithms and Cosine Similarity, the system analyzes movie metadata (such as overviews and descriptions) to find and suggest movies similar to your favorites. 

The API layer is built with **FastAPI** for high performance and asynchronous request handling, and integrates with the **TMDB (The Movie Database) API** to fetch rich, real-time movie details, posters, and backdrops.

## ✨ Features

- ⚡ **Lightning Fast Inference:** Model components (TF-IDF matrix & vectorizer) are pre-trained and serialized using `pickle` for sub-millisecond similarity lookups.
- 🎨 **Rich Movie Data:** Automatically enriches recommendations with TMDB posters, backdrops, release dates, and genres.
- 🔗 **RESTful API:** Clean, structured FastAPI endpoints returning fully-typed Pydantic JSON responses.
- 🛡️ **Robust Error Handling:** Asynchronous TMDB API calls with comprehensive HTTP error handling and status code propagation.

## 📂 Project Structure

| File | Description |
|------|-------------|
| 📜 `main.py` | FastAPI application routing, Pydantic data models, and TMDB integration logic. |
| 📊 `movies_metadata.csv` | The core dataset containing raw metadata about the movies used for training. |
| 📦 `df.pkl` | Serialized pandas DataFrame with preprocessed and cleaned movie data. |
| 🧮 `tfidf.pkl` | The trained TF-IDF Vectorizer used to extract text features. |
| 🕸️ `tfidf_matrix.pkl` | The transformed TF-IDF sparse matrix representing movie feature vectors. |
| 📇 `indices.pkl` | A title-to-index mapping dictionary for `O(1)` movie lookups during inference. |
| ⚙️ `.env` | Environment configuration (requires `API_KEY` for TMDB access). |

## 🧠 How the Engine Works

1. **Text Vectorization:** The system reads textual metadata for thousands of movies and converts them into numerical vectors using the TF-IDF statistical measure.
2. **Similarity Computation:** When a user searches for a movie, the engine calculates the **Cosine Similarity** between that movie's vector and every other movie in the dataset.
3. **Ranking & Enrichment:** The top `N` most similar movies are extracted, and their IDs are sent asynchronously to TMDB to fetch high-quality visual assets before returning the response to the client.

## 🚦 Status

✅ **Model Trained:** The NLP models are fully trained and serialized.
✅ **API Functional:** The FastAPI wrapper is implemented with asynchronous TMDB fetching.
✅ **Ready for Deployment:** Code is optimized, typed, and formatted to industry standards.

---
<div align="center">
  <i>Built with ❤️ for Movie Enthusiasts • Powered by TMDB</i>
</div>
