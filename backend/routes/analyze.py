from fastapi import APIRouter

from backend.schemas.music_task import AnalyzeRequest, AnalyzeResponse
from backend.services.clap_service import analyze_audio


router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    return analyze_audio(request)
