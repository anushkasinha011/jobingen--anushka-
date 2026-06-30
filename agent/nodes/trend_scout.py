from adapters.google_trends import get_google_trends
from adapters.news import get_latest_news
from adapters.reddit import fetch_trending_posts


def trend_scout_node(state):
    """
    Collect trends from different sources and store them in state.
    """

    trends = get_google_trends()

    news = get_latest_news()

    reddit = fetch_trending_posts(
        subreddit_name="marketing",
        limit=10,
        time_filter="day"
    )

    # Convert Google Trends into signals
    signals = []

    for trend in trends:
        signals.append({
            "topic": trend,
            "score": 1
        })

    state["trends"] = trends
    state["news"] = news
    state["reddit"] = reddit
    state["signals"] = signals

    return state