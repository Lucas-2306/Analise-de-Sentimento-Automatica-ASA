from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    query: str
    pages: int = 1