import os
import praw
from dotenv import load_dotenv

load_dotenv()

REDDIT_ENABLED = all([
    os.getenv("REDDIT_CLIENT_ID"),
    os.getenv("REDDIT_CLIENT_SECRET"),
    os.getenv("REDDIT_USERNAME"),
    os.getenv("REDDIT_PASSWORD"),
])


def get_reddit_client():
    if not REDDIT_ENABLED:
        return None
    try:
        return praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
            user_agent=os.getenv("REDDIT_USER_AGENT", "JobInGenMarketingAgent/0.1"),
        )
    except Exception as e:
        print(f"[reddit.py] Failed to initialize Reddit client: {e}")
        return None


def fetch_trending_posts(subreddit_name: str, limit: int = 10, time_filter: str = "day"):
    """
    Fetch top trending posts from a subreddit.
    Returns an empty list (with a warning) if Reddit isn't configured yet,
    so the rest of the pipeline can run without it.
    """
    reddit = get_reddit_client()
    if reddit is None:
        print(f"[reddit.py] Reddit not configured — skipping r/{subreddit_name}")
        return []

    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = []
        for submission in subreddit.top(time_filter=time_filter, limit=limit):
            posts.append({
                "title": submission.title,
                "score": submission.score,
                "num_comments": submission.num_comments,
                "url": submission.url,
                "permalink": f"https://reddit.com{submission.permalink}",
                "created_utc": submission.created_utc,
                "selftext": submission.selftext[:500] if submission.selftext else "",
                "subreddit": subreddit_name,
            })
        return posts
    except Exception as e:
        print(f"[reddit.py] Error fetching from r/{subreddit_name}: {e}")
        return []


if __name__ == "__main__":
    results = fetch_trending_posts("jobs", limit=5, time_filter="day")
    if results:
        for r in results:
            print(f"[{r['score']}] {r['title']} ({r['num_comments']} comments)")
    else:
        print("No Reddit data available (not configured or error occurred).")