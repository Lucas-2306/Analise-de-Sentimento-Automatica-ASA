from scraping.collectors.post_collector import collect_posts
from backend.services.aggregator import aggregate_results

predictor = None


def get_predictor():
    """
    Lazy-load the sentiment model once.
    """

    global predictor

    if predictor is None:
        from models.inference.sentiment_predictor import SentimentPredictor
        predictor = SentimentPredictor()

    return predictor


def run_analysis(query: str, pages: int = 1):

    items = collect_posts(query=query, pages=pages)

    texts = [i["text"] for i in items]
    dates = [i["date"] for i in items]

    if not texts:
        return {
            "query": query,
            "total_texts": 0,
            "positive": 0,
            "neutral": 0,
            "negative": 0,
            "results": []
        }

    model = get_predictor()

    predictions = model.predict(texts)

    for p, d in zip(predictions, dates):
        p["date"] = d

    counts, timeline = aggregate_results(predictions)

    return {
        "query": query,
        "total_texts": len(texts),
        "positive": counts["positive"],
        "neutral": counts["neutral"],
        "negative": counts["negative"],
        "timeline": timeline,
        "results": predictions
    }