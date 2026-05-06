from fastapi import APIRouter

from backend.schemas.music_task import VisualizeRequest, VisualizeResponse
from backend.services.seeddance_service import build_visual_prompt


router = APIRouter()


@router.post("/visualize", response_model=VisualizeResponse)
def visualize(request: VisualizeRequest) -> VisualizeResponse:
    return build_visual_prompt(request)
