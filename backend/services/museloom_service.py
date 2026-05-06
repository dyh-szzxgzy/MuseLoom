from backend.schemas.music_task import GenerateRequest, GenerateResponse


def generate_music(request: GenerateRequest) -> GenerateResponse:
    revised_prompt = ", ".join(request.prompt_tags)
    melody_note = "保留原始旋律骨架" if request.preserve_melody else "允许较大幅度改写旋律"
    return GenerateResponse(
        status="mock_ready",
        revised_prompt=f"{revised_prompt}, 生成策略: {melody_note}",
        output_audio="data/samples/generated_demo.wav",
        note="Current scaffold returns a placeholder output for roadshow demos.",
    )
