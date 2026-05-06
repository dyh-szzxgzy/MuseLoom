from fastapi import APIRouter

from backend.schemas.music_task import GenerateRequest, GenerateResponse
from backend.services.museloom_service import generate_music


router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    return generate_music(request)
