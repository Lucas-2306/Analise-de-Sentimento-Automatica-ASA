import os
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from models.training.dataset_loader import load_dataset


MODEL_PATH = "models/saved_models/sentiment_model.joblib"


def train_model(dataset_path: str):

    texts, labels = load_dataset(dataset_path)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(texts, labels)

    os.makedirs("models/saved_models", exist_ok=True)

    joblib.dump(pipeline, MODEL_PATH)

    print("Model saved to:", MODEL_PATH)


if __name__ == "__main__":

    dataset_path = "data/raw/sentiment_dataset.csv"

    train_model(dataset_path)