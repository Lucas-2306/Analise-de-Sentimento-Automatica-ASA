import re


URL_PATTERN = re.compile(r"https?://\S+")
MULTI_SPACE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    """
    Basic cleaning for Reddit text.
    """

    if not text:
        return ""

    text = text.lower()

    text = URL_PATTERN.sub("", text)

    text = MULTI_SPACE.sub(" ", text)

    text = text.strip()

    return text