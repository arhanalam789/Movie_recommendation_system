import os
import pickle
from typing import Optional,List,Tuple,Any

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity

from fastapi import FastAPI, HTTPException,Query
import pandas as pd
import httpx

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
tmdb_base_url = "https://api.themoviedb.org/3"
tmdb_image_base_url = "https://image.tmdb.org/t/p/w500"

if not api_key:
    raise RuntimeError("API_KEY not found in .env file")


app = FastAPI(
    title="Movie Recommendation System",
    description="API for movie recommendation system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base_dir = os.path.dirname(os.path.abspath(__file__))

df_path = os.path.join(base_dir,"df.pkl")

indices_path = os.path.join(base_dir,"indices.pkl")

tfidf_matrix_path = os.path.join(base_dir,"tfidf_matrix.pkl")

tfidf_path = os.path.join(base_dir,"tfidf.pkl")

df:Optional[pd.DataFrame] = None
indices_obj:any = None
tfidf_matrix_obj:any = None
tfidf_obj:any = None

title_to_idx: Optional[dict[str, int]] = None

class TmdbMovieCard(BaseModel):
    tmdb_id: int
    title: str
    poster_url: Optional[str] = None
    release_date: Optional[str] = None
    vote_average: Optional[float] = None
    

class TmdbMovieDetails(BaseModel):
    tmdb_id: int
    title: str
    overview: Optional[str] = None
    poster_url: Optional[str] = None
    release_date: Optional[str] = None
    backdrop_url: Optional[str] = None
    genres: list[dict] = []

class TfidfRecMovie(BaseModel):
    title: str
    score: float
    tmdb: Optional[list[TmdbMovieCard]] = None
    
    
    
class SearchBundleResponse(BaseModel):
    query: str
    movie_details: TmdbMovieDetails
    tfidf_recommendations: list[TfidfRecMovie]
    genere_recommendation: list[TmdbMovieCard]
    

def norm_title(title:str)->str:
    return title.lower().strip()

def make_img_url(path:Optional[str])->Optional[str]:
    if not path:
        return None
    return f"{tmdb_image_base_url}{path}" 

async def tmdb_get(path:str,params:Optional[dict]=None)->Optional[dict]:
    q = dict(params)
    q["api_key"] = api_key
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{tmdb_base_url}{path}",params=q)
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,detail=f"TMDB error: {e}")
    except httpx.RequestException as e:
        raise HTTPException(status_code=500,detail=f"TMDB request failed: {e}")
    if resp.status_code == 200:
        return resp.json()
    else:
        raise HTTPException(status_code=resp.status_code,detail=f"TMDB error: {resp.status_code}")