from backend.schemas.music_task import AnalyzeRequest, AnalyzeResponse


def analyze_audio(request: AnalyzeRequest) -> AnalyzeResponse:
    source_name = request.audio_path or request.audio_name or "demo_audio.wav"
    classroom_context = request.classroom_context or "高中音乐课堂"
    context_teaching_map = {
        "高中音乐鉴赏课": "适合用于课堂中的风格迁移和情绪表达分析。",
        "高中作曲入门课": "适合引导学生观察旋律骨架与风格重构之间的关系。",
        "社团展示": "适合做跨模态展示，便于快速吸引观众理解音乐气质。",
    }
    teaching_hint = context_teaching_map.get(
        classroom_context,
        "适合用于课堂中的风格迁移和情绪表达分析。",
    )
    return AnalyzeResponse(
        audio_name=source_name,
        tempo_bpm=92,
        style_tags=["印象派", "室内乐", "抒情"],
        mood_tags=["平静", "温暖", "沉思"],
        teaching_hint=teaching_hint,
        feature_profile=[62, 48, 88, 40, 76],
        spectrum_bins=[0.16, 0.24, 0.38, 0.52, 0.66, 0.72, 0.68, 0.58, 0.49, 0.43, 0.35, 0.28],
        status="mock_ready",
    )
