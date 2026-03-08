import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://newsapi.org/v2/everything"


def get_news(query: str, page: int = 1, page_size: int = 100):

    api_key = os.getenv("NEWS_API_KEY")

    params = {
        "q": query,
        "pageSize": page_size,
        "page": page,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    return response.json()