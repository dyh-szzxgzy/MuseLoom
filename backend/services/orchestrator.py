from backend.schemas.music_task import (
    AnalyzeRequest,
    DemoFlowRequest,
    DemoFlowResponse,
    GenerateRequest,
    PromptRevisionRequest,
    VisualizeRequest,
)
from backend.services.clap_service import analyze_audio
from backend.services.llm_service import revise_prompt
from backend.services.museloom_service import generate_music
from backend.services.seeddance_service import build_visual_prompt


def run_demo_flow(request: DemoFlowRequest) -> DemoFlowResponse:
    analysis = analyze_audio(
        AnalyzeRequest(
            audio_name=request.audio_name,
            audio_path=request.audio_path,
            classroom_context=request.classroom_context,
        )
    )

    revision = revise_prompt(
        PromptRevisionRequest(
            style_tags=analysis.style_tags,
            mood_tags=analysis.mood_tags,
            teaching_hint=analysis.teaching_hint,
            classroom_context=request.classroom_context or "高中音乐鉴赏课",
            user_prompt_overrides=request.prompt_tags,
        )
    )

    generation = generate_music(
        GenerateRequest(
            prompt_tags=revision.prompt_tags,
            source_audio=analysis.audio_name,
            preserve_melody=request.preserve_melody,
        )
    )

    visualization = build_visual_prompt(
        VisualizeRequest(
            style_tags=analysis.style_tags,
            mood_tags=analysis.mood_tags,
            visual_focus="原曲与重构曲目的并置对比",
        )
    )

    return DemoFlowResponse(
        analysis=analysis,
        generation=generation,
        visualization=visualization,
    )
