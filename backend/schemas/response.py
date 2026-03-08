from pydantic import BaseModel
from typing import List


class SentimentItem(BaseModel):
    text: str
    sentiment: str
    score: float


class AnalyzeResponse(BaseModel):
    query: str
    total_texts: int
    positive: int
    neutral: int
    negative: int
    results: List[SentimentItem]