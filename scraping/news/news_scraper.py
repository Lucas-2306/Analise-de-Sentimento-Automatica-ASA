from .news_client import get_news


def search_articles(query: str, pages: int = 1):

    # Free plan allows only page 1
    pages = min(pages, 1)

    articles = []

    for page in range(1, pages + 1):

        data = get_news(query=query, page=page)

        for article in data["articles"]:

            articles.append(
                {
                    "title": article["title"],
                    "description": article["description"],
                    "source": article["source"]["name"],
                    "url": article["url"],
                    "published_at": article["publishedAt"],
                }
            )

    return articles