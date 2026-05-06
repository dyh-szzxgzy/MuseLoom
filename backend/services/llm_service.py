from backend.schemas.music_task import PromptRevisionRequest, PromptRevisionResponse


def build_prompt_payload(request: PromptRevisionRequest) -> dict:
    return {
        "model": "DeepSeek V4",
        "purpose": "music_prompt_revision",
        "style_tags": request.style_tags,
        "mood_tags": request.mood_tags,
        "teaching_hint": request.teaching_hint,
        "classroom_context": request.classroom_context,
        "user_prompt_overrides": request.user_prompt_overrides,
    }


def revise_prompt(request: PromptRevisionRequest) -> PromptRevisionResponse:
    style_text = "、".join(request.style_tags or ["印象派"])
    mood_text = "、".join(request.mood_tags or ["平静"])
    override_text = "；".join(request.user_prompt_overrides) if request.user_prompt_overrides else ""
    prompt_tags = [
        f"风格: {style_text}",
        f"情绪: {mood_text}",
        f"课堂语境: {request.classroom_context or '高中音乐鉴赏课'}",
        f"教学提示: {request.teaching_hint or '对比不同风格的表达差异'}",
    ]
    if override_text:
        prompt_tags.append(f"用户补充: {override_text}")

    return PromptRevisionResponse(
        status="mock_ready",
        revised_prompt="; ".join(prompt_tags) + "；保留原始旋律骨架",
        prompt_tags=prompt_tags,
        provider="DeepSeek V4 placeholder",
    )
