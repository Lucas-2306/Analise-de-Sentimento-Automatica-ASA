import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SentimentPredictor:

    def __init__(self):

        self.api_url = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment-latest"

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
            "Content-Type": "application/json"
        }

    def predict(self, texts):

        formatted = []

        for text in texts:

            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={
                    "inputs": text,
                    "options": {"wait_for_model": True}
                }
            )

            if response.status_code != 200:
                print("HF ERROR:", response.status_code, response.text)
                formatted.append({
                    "text": text,
                    "sentiment": "neutral",
                    "score": 0.0
                })
                continue

            try:
                result = response.json()
            except Exception:
                print("RAW RESPONSE:", response.text)
                formatted.append({
                    "text": text,
                    "sentiment": "neutral",
                    "score": 0.0
                })
                continue

            try:
                # Handle both formats
                if isinstance(result[0], list):
                    scores = result[0]
                else:
                    scores = result

                best = max(scores, key=lambda x: x["score"])

                formatted.append({
                    "text": text,
                    "sentiment": best["label"].lower(),
                    "score": float(best["score"])
                })

            except Exception:
                print("PARSE ERROR:", result)
                formatted.append({
                    "text": text,
                    "sentiment": "neutral",
                    "score": 0.0
                })

        return formatted