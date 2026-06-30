import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_latest_news(query="Artificial Intelligence"):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return []

    data = response.json()

    headlines = []

    for article in data["articles"]:
        headlines.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"]
        })

    return headlines


if __name__ == "__main__":
    news = get_latest_news()

    for item in news:
        print(item)