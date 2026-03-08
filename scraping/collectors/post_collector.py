from scraping.news.news_scraper import search_articles
from scraping.cleaners.text_cleaner import clean_text


def collect_posts(query: str, pages: int = 1):

    raw_articles = search_articles(query=query, pages=pages)

    items = []

    for article in raw_articles:

        if article["title"]:
            items.append({
                "text": article["title"],
                "date": article["published_at"]
            })

        if article["description"]:
            items.append({
                "text": article["description"],
                "date": article["published_at"]
            })

    return items