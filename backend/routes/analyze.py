from fastapi import APIRouter

from backend.schemas.request import AnalyzeRequest
from backend.services.pipeline import run_analysis


router = APIRouter()


@router.post("/analyze")
def analyze(req: AnalyzeRequest):

    result = run_analysis(
        query=req.query,
        pages=req.pages
    )

    return result