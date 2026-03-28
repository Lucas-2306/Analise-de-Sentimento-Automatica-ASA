import os
import requests
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

load_dotenv()


class SentimentPredictor:

    def __init__(self):

        self.api_url = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment-latest"

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
            "Content-Type": "application/json"
        }

    def predict_one(self, text):

        if len(text.strip()) < 20:
            return {
                "text": text,
                "sentiment": "neutral",
                "score": 0.0
            }

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={
                    "inputs": text,
                    "options": {"wait_for_model": True}
                }
            )

            if response.status_code != 200:
                return {
                    "text": text,
                    "sentiment": "neutral",
                    "score": 0.0
                }

            result = response.json()

            if not isinstance(result, list):
                return {
                    "text": text,
                    "sentiment": "neutral",
                    "score": 0.0
                }

            scores = result[0] if isinstance(result[0], list) else result

            labels = {
                "positive": 0.0,
                "neutral": 0.0,
                "negative": 0.0
            }

            for x in scores:
                labels[x["label"].lower()] = x["score"]

            # 🔥 weighted score
            weighted_score = labels["positive"] - labels["negative"]

            # 🔥 classification
            if weighted_score > 0.2:
                sentiment = "positive"
            elif weighted_score < -0.2:
                sentiment = "negative"
            else:
                sentiment = "neutral"

            return {
                "text": text,
                "sentiment": sentiment,
                "score": float(weighted_score)
            }

        except Exception:
            return {
                "text": text,
                "sentiment": "neutral",
                "score": 0.0
            }

    def predict(self, texts):

        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(self.predict_one, texts))

        return results