<div align="center">
  <img src="https://img.icons8.com/nolan/256/movie-projector.png" width="100" />
  <h1>🎬 Cinemagic Movie Recommender</h1>
  <p><i>A premium, fast, and intelligent hybrid movie recommendation system built with FastAPI, Streamlit, and TMDB.</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/TMDB-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" />
  </p>
</div>

---

## 🚀 Overview

Cinemagic is a full-stack movie recommendation platform. It combines a **content-based NLP engine** (using TF-IDF and Cosine Similarity) with real-time data from **TMDB**. The system provides a Netflix-style premium UI where users can search for movies, see trending feeds, and get deep plot-based recommendations instantly.

## ✨ Key Features

- 🤖 **Trained NLP Model:** Uses serialized TF-IDF matrices (`pickle` files) to recommend movies based on plot similarity.
- ⚡ **Lightning Fast:** Optimized with `asyncio` for parallel API fetching—recommendations load in under 1 second.
- 🎨 **Premium UI/UX:** A modern Streamlit interface with dark mode, glassmorphism, and responsive movie grids.
- 🔍 **Fuzzy Search:** Robust title matching that finds the right movie even with slight typos or mismatched formats.
- 🔗 **Smart Navigation:** Unique ID-based recommendation logic that works seamlessly as you jump from movie to movie.
- 🌐 **Render Ready:** Includes `render.yaml` and `.python-version` for easy cloud deployment.

## 📂 Project Structure

| File | Description |
|------|-------------|
| 🎨 `app.py` | Streamlit Frontend - Premium UI, State Management, and API integration. |
| 📜 `main.py` | FastAPI Backend - NLP Engine, TF-IDF calculation, and TMDB wrapper. |
| 📊 `movies_metadata.csv` | Core dataset used for model training. |
| 📦 `df.pkl`, `tfidf.pkl`, etc. | Serialized trained model components for fast inference. |
| ⚙️ `render.yaml` | Deployment configuration for Render.com. |

## 🛠️ Local Setup

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/arhanalam789/Movie_recommendation_system
   cd Movie_recommendation_system
   ```

2. **Environment Variables:**
   Create a `.env` file and add your TMDB API Key:
   ```env
   API_KEY=your_tmdb_api_key_here
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   Open two terminals:
   - **Backend:** `uvicorn main:app --port 8000`
   - **Frontend:** `streamlit run app.py`

---
<div align="center">
  <i>Built with ❤️ for Movie Enthusiasts • Powered by TMDB</i>
</div>
