from models.inference.sentiment_predictor import SentimentPredictor


if __name__ == "__main__":

    predictor = SentimentPredictor()

    texts = [
        "Tesla stock surged after earnings",
        "Tesla faces investigation over autopilot crash",
        "Tesla announced a new battery technology"
    ]

    results = predictor.predict(texts)

    for r in results:
        print(r)