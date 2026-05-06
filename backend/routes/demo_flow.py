from fastapi import APIRouter

from backend.schemas.music_task import DemoFlowRequest, DemoFlowResponse
from backend.services.orchestrator import run_demo_flow


router = APIRouter()


@router.post("/demo-flow", response_model=DemoFlowResponse)
def demo_flow(request: DemoFlowRequest) -> DemoFlowResponse:
    return run_demo_flow(request)
