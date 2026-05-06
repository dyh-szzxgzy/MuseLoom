from fastapi import FastAPI

from backend.routes.analyze import router as analyze_router
from backend.routes.demo_flow import router as demo_flow_router
from backend.routes.generate import router as generate_router
from backend.routes.visualize import router as visualize_router


app = FastAPI(
    title="MuseLoom API",
    description="Presentation-oriented mock API for the MuseLoom teaching platform.",
    version="0.1.0",
)

app.include_router(analyze_router, prefix="/api")
app.include_router(demo_flow_router, prefix="/api")
app.include_router(generate_router, prefix="/api")
app.include_router(visualize_router, prefix="/api")


@app.get("/")
def read_root() -> dict:
    return {
        "project": "MuseLoom",
        "status": "scaffold_ready",
        "message": "Use /api/demo-flow or individual endpoints for the MuseLoom demo.",
    }
