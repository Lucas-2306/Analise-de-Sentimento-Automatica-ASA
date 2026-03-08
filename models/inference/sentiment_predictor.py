from transformers import pipeline


class SentimentPredictor:

    def __init__(self):

        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

        self.classifier = pipeline(
            "sentiment-analysis",
            model=self.model_name,
            tokenizer=self.model_name,
            truncation=True,
            batch_size=32
        )

    def predict(self, texts):

        results = self.classifier(texts)

        formatted = []

        for text, res in zip(texts, results):

            formatted.append({
                "text": text,
                "sentiment": res["label"],
                "score": float(res["score"])
            })

        return formatted