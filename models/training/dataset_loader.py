import pandas as pd


def load_dataset(path: str):
    """
    Load sentiment dataset.

    Expected CSV format:
    text,sentiment
    """

    df = pd.read_csv(path)

    if "text" not in df.columns or "sentiment" not in df.columns:
        raise ValueError("Dataset must contain 'text' and 'sentiment' columns")

    texts = df["text"].astype(str).tolist()
    labels = df["sentiment"].tolist()

    return texts, labels