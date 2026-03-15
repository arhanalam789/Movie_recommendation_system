import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-system-n1sj.onrender.com"
# API_BASE = "http://127.0.0.1:8000"  # Fallback for local testing

TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Cinemagic Recommender", page_icon="🍿", layout="wide")

# =============================
# STYLES (Premium Modern UI)
# =============================
st.markdown(
    """
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

/* Global Reset & Base */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
}
.stApp {
    background-color: #0b0f19;
    color: #e2e8f0;
}

/* Hide default streamlit marks */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Container tuning */
.block-container { 
    padding-top: 2rem !important; 
    padding-bottom: 4rem !important; 
    max-width: 1400px; 
}

/* Custom Typography */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

h1 {
    font-size: 3rem !important;
    background: -webkit-linear-gradient(45deg, #e50914, #ff8a00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0 !important;
}

.subtext {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 400;
}

/* Movie Grid */
.movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 24px;
    margin-top: 20px;
    margin-bottom: 40px;
}
@media (min-width: 1200px) {
    .movie-grid {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}

/* Movie Card */
.movie-card-link {
    text-decoration: none !important;
    color: inherit !important;
    display: block;
    height: 100%;
}

.movie-card {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 16px;
    overflow: hidden;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
}

.movie-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(229, 9, 20, 0.2);
    border-color: rgba(229, 9, 20, 0.4);
}

.poster-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 2 / 3;
    overflow: hidden;
    background: #1e293b;
}

.movie-poster {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.movie-card:hover .movie-poster {
    transform: scale(1.05);
}

.badge-rating {
    position: absolute;
    top: 10px;
    right: 10px;
    background: rgba(15, 23, 42, 0.85);
    color: #fbbf24;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 700;
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255,255,255,0.1);
    display: flex;
    align-items: center;
    gap: 4px;
}

.movie-info {
    padding: 16px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.movie-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #f8fafc;
    line-height: 1.3;
    margin-bottom: 6px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}

.movie-year {
    font-size: 0.9rem;
    color: #94a3b8;
    font-weight: 500;
}

/* Detail view */
.detail-header {
    background: rgba(30, 41, 59, 0.4);
    border-radius: 24px;
    padding: 32px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.detail-title {
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 12px;
    color: #fff;
}

.badge {
    background: #e50914; 
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-right: 12px;
    display: inline-block;
    letter-spacing: 0.5px;
}
.badge-secondary {
    background: #334155;
}

.overview-text {
    font-size: 1.15rem;
    line-height: 1.7;
    color: #cbd5e1;
    margin-top: 24px;
}

.detail-poster {
    border-radius: 16px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.1);
    width: 100%;
    display: block;
}

/* Buttons */
div.stButton > button {
    background: #1e293b;
    color: #fff;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 8px 16px;
    font-weight: 600;
    transition: all 0.3s;
}
div.stButton > button:hover {
    background: #e50914;
    border-color: #e50914;
    color: white;
    box-shadow: 0 4px 12px rgba(229, 9, 20, 0.3);
}

/* Back button specific */
.btn-back > div, .btn-back > div > div > button {
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    color: #cbd5e1 !important;
}
.btn-back > div > div > button:hover {
    background: rgba(255,255,255,0.1) !important;
    color: #fff !important;
}

/* Input boxes */
div.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
    border: 1px solid #334155;
    padding: 14px;
    font-size: 1.1rem;
}
div.stTextInput > div > div > input:focus {
    border-color: #e50914;
    box-shadow: 0 0 0 1px #e50914;
}

/* Select boxes */
div.stSelectbox > div > div {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
    border: 1px solid #334155;
}
</style>
""",
    unsafe_allow_html=True,
)


# =============================
# STATE + ROUTING
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

# Using the modern query_params API
qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")

if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home(clear_search=True):
    st.session_state.view = "home"
    if clear_search:
        if "search_query" in st.session_state:
            st.session_state.search_query = ""
    
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=60)
def api_get_json(path: str, params: dict | None = None):
    try:
        # Tries Render first, then falls back to Localhost if it's down
        urls_to_try = [API_BASE, "http://127.0.0.1:8000"]
        
        last_err = None
        for base_url in urls_to_try:
            try:
                r = requests.get(f"{base_url}{path}", params=params, timeout=12)
                if r.status_code < 400:
                    return r.json(), None
                else:
                    last_err = f"HTTP {r.status_code}: {r.text[:200]}"
            except requests.exceptions.RequestException as e:
                last_err = str(e)
                continue
                
        return None, f"All requests failed. Last error: {last_err}"
    except Exception as e:
        return None, f"Unexpected Error: {e}"


def poster_grid(cards, columns=5):
    """Renders a beautiful responsive grid for movie cards using st.columns."""
    if not cards:
        st.info("No available recommendations.")
        return

    # Calculate rows
    for i in range(0, len(cards), columns):
        cols = st.columns(columns)
        for j, col in enumerate(cols):
            if i + j < len(cards):
                m = cards[i + j]
                tmdb_id = m.get("tmdb_id")
                title = m.get("title", "Untitled").replace("'", "&#39;").replace('"', "&quot;")
                poster = m.get("poster_url")
                year = m.get("release_date", "")[:4] if m.get("release_date") else ""
                vote = m.get("vote_average", 0)
                
                img_src = poster if poster else "https://via.placeholder.com/500x750/1e293b/ffffff?text=No+Poster"
                
                rating_badge = f"<div class='badge-rating'>⭐ {round(vote, 1) if vote else 'NR'}</div>" 
                
                card_html = f"""
                <a href="?view=details&id={tmdb_id}" target="_self" class="movie-card-link">
                    <div class="movie-card">
                        <div class="poster-wrapper">
                            <img src="{img_src}" class="movie-poster" alt="{title}" loading="lazy" />
                            {rating_badge}
                        </div>
                        <div class="movie-info">
                            <div class="movie-title">{title}</div>
                            <div class="movie-year">{year}</div>
                        </div>
                    </div>
                </a>
                """
                with col:
                    st.markdown(card_html, unsafe_allow_html=True)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                    "release_date": tmdb.get("release_date"),
                    "vote_average": tmdb.get("vote_average"),
                }
            )
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 12):
    """
    Returns:
      suggestions: list[(label, tmdb_id)]
      cards: list[{tmdb_id,title,poster_url}]
    """
    keyword_l = keyword.strip().lower()

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            if not title or not m.get("id"): continue
            items.append({
                "tmdb_id": int(m["id"]),
                "title": title,
                "poster_url": f"{TMDB_IMG}{m['poster_path']}" if m.get("poster_path") else None,
                "release_date": m.get("release_date", ""),
                "vote_average": m.get("vote_average", 0),
            })
    else:
        return [], []

    matched = [x for x in items if keyword_l in x["title"].lower()]
    others = [x for x in items if keyword_l not in x["title"].lower()]
    final_list = matched + others

    suggestions = []
    for x in final_list[:8]:
        year = x["release_date"][:4] if x.get("release_date") else ""
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    return suggestions, final_list[:limit]


# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🍿 Welcome")
        st.write("Discover the best movies across various categories, powered by a personalized hybrid recommender engine.")
        
        st.markdown("---")
        st.markdown("### 🎬 Explore Categories")
        
        home_category = st.selectbox(
            "Select Feed",
            [
                ("Trending Today", "trending"),
                ("Popular This Week", "popular"),
                ("Top Rated Masters", "top_rated"),
                ("Playing in Theaters", "now_playing"),
                ("Upcoming Releases", "upcoming"),
            ],
            format_func=lambda x: x[0],
            index=0,
            on_change=lambda: st.session_state.update({"search_query": ""})
        )
        cat_value = home_category[1]

    # Main Header
    st.markdown("<h1>Cinemagic <span style='font-weight: 300'>Recommender</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>Find top tier recommendations spanning genres and taste boundaries instantly.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Search Bar
    typed = st.text_input(
        "🔎 Search by Title", 
        placeholder="Type a movie name: Avengers, Interstellar, The Matrix...",
        label_visibility="collapsed",
        key="search_query"
    )

    # Search Results Mode
    if typed.strip():
        col_clear, _ = st.columns([1, 5])
        with col_clear:
            if st.button("❌ Clear Search"):
                st.session_state.search_query = ""
                st.rerun()

        if len(typed.strip()) < 2:
            st.caption("Keep typing...")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"⚠️ Search failed to connect. Is the backend running? ({err})")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=12)

                if suggestions:
                    st.markdown("### 🎯 Quick Results", unsafe_allow_html=True)
                    poster_grid(cards)
                else:
                    st.info("No matching movies found. Try another keyword.")

    # Generic Feed Mode
    else:
        st.markdown(f"### 🔥 {home_category[0]}")
        
        home_cards, err = api_get_json("/home", params={"category": cat_value, "limit": 30})
        
        if err or not home_cards:
            st.error(f"⚠️ Failed to gather feed: {err}. Make sure your FastAPI backend is running.")
            st.stop()

        poster_grid(home_cards)


# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        goto_home()
        st.stop()
        
    # Top nav bar 
    st.markdown("<div class='btn-back'>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        goto_home()
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Fetch Details
    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    
    if err or not data:
        st.error(f"⚠️ Could not load details: {err}")
        st.stop()

    # Backdrop setup (inject as banner if present)
    backdrop = data.get("backdrop_url")
    if backdrop:
        st.markdown(f'''
        <div style="
            width: 100%;
            height: clamp(300px, 40vh, 500px);
            background-image: linear-gradient(to top, #0b0f19 0%, rgba(11, 15, 25, 0.4) 100%), url('{backdrop}');
            background-size: cover;
            background-position: center 20%;
            border-radius: 24px;
            margin-bottom: -150px;
            position: relative;
            z-index: 0;
            opacity: 0.8;
            mask-image: linear-gradient(to bottom, black 50%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 100%);
        "></div>
        ''', unsafe_allow_html=True)

    # Layout: Poster LEFT, Details RIGHT
    st.markdown("<div class='detail-header'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2.5], gap="large")

    with col1:
        img_src = data.get("poster_url") or "https://via.placeholder.com/500x750/1e293b/ffffff?text=No+Poster"
        st.markdown(f"""
            <img src="{img_src}" class="detail-poster" />
        """, unsafe_allow_html=True)

    with col2:
        title = data.get("title", "Unknown Title").replace("'", "&#39;")
        year = data.get("release_date", "")[:4] if data.get("release_date") else ""
        
        title_disp = f"{title} ({year})" if year else title
        st.markdown(f"<div class='detail-title'>{title_disp}</div>", unsafe_allow_html=True)
        
        # Genres Badges
        genres_html = ""
        for g in data.get("genres", []):
            genres_html += f"<span class='badge'>{g['name']}</span>"
             
        st.markdown(f"<div>{genres_html}</div>", unsafe_allow_html=True)
        
        overview = data.get('overview', 'No overview provided.').replace("'", "&#39;")
        st.markdown(f"<div class='overview-text'>{overview}</div>", unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)


    # Recommendations (TF-IDF + Genre)
    title_for_rec = data.get("title", "").strip()
    
    if title_for_rec:
        with st.spinner("Finding perfect matches for you..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title_for_rec, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            
            tfidf_recs = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            genre_recs = bundle.get("genre_recommendations", [])
            
            # Use tabs for a cleaner look
            tab1, tab2 = st.tabs(["✨ More Like This (Similar Plot)", "🎭 Related by Genre"])
            
            with tab1:
                if tfidf_recs:
                    poster_grid(tfidf_recs)
                else:
                    st.info("No detailed plot matches found. Switch to Genre tab.")
                    
            with tab2:
                if genre_recs:
                    poster_grid(genre_recs)
                else:
                    st.info("No genre matches found.")
        else:
            # Fallback
            st.markdown("### 🎭 Recommended for You")
            genre_only, err3 = api_get_json("/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18})
            if not err3 and genre_only:
                poster_grid(genre_only)
            else:
                st.warning("Connections are slightly unstable; recommendations unavailable right now.")
    else:
         st.warning("Movie title missing. Cannot fetch recommendations.")
