from backend.config import settings
from backend.schemas.music_task import VisualizeRequest, VisualizeResponse
from models.seeddance_integration.client import DiffusionClientConfig, generate_image


def build_visual_payload(request: VisualizeRequest) -> dict:
    return {
        "provider": "SeedDance 2.0",
        "style_tags": request.style_tags,
        "mood_tags": request.mood_tags,
        "visual_focus": request.visual_focus or "课堂中的原曲与重构曲对比",
        "output_format": "visual_prompt_text",
    }


def build_visual_prompt(request: VisualizeRequest) -> VisualizeResponse:
    tags = "、".join(request.mood_tags or ["平静", "层次感"])
    style = "、".join(request.style_tags or ["印象派"])
    visual_focus = request.visual_focus or "课堂中的原曲与重构曲对比"
    prompt = (
        f"一间用于音乐教学展示的空间，光影柔和，画面呈现{style}风格，"
        f"以流动的色块表达{tags}的音乐情绪，构图强调{visual_focus}。"
    )

    if (
        settings.model_mode != "mock"
        and settings.seeddance_api_key
        and settings.seeddance_api_base_url
    ):
        config = DiffusionClientConfig(
            api_key=settings.seeddance_api_key,
            base_url=settings.seeddance_api_base_url,
            submit_path=settings.seeddance_submit_path,
            result_path_template=settings.seeddance_result_path_template,
        )
        try:
            image_result = generate_image(prompt=prompt, config=config)
            return VisualizeResponse(
                status=str(image_result.get("status", "unknown")),
                visual_prompt=prompt,
                provider=str(image_result.get("provider", "SeedDance 2.0")),
                image_url=image_result.get("image_url"),
                image_path=image_result.get("image_path"),
                task_id=image_result.get("task_id"),
            )
        except Exception:
            pass

    return VisualizeResponse(
        status="mock_ready",
        visual_prompt=prompt,
        provider="SeedDance 2.0 placeholder",
        image_path="demo/sample_outputs/visual_demo.png",
    )
