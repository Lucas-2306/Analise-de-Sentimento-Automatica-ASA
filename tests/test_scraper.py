from scraping.collectors.post_collector import collect_posts


if __name__ == "__main__":

    articles = collect_posts("Tesla", pages=1)

    for a in articles[:10]:
        print(a)