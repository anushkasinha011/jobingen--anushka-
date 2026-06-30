import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Signal sourcing config
TRENDS_KEYWORDS = ["job search", "career change", "resume tips", "layoffs", "hiring"]
NEWS_QUERY = "job market OR hiring OR layoffs OR career"
REDDIT_SUBREDDITS = ["jobs", "careerguidance", "careeradvice", "resumes"]

# Scoring thresholds
TOP_SIGNALS_COUNT = 5
MIN_COMPOSITE_SCORE = 0.4

# LLM config
GEMINI_MODEL = "gemini-1.5-pro"