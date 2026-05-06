def generate_visual_prompt(style_tags: list[str], mood_tags: list[str]) -> str:
    style_text = "、".join(style_tags or ["印象派"])
    mood_text = "、".join(mood_tags or ["平静"])
    return (
        f"以{style_text}风格构建教学场景，用流动的色彩呈现{mood_text}的音乐情绪，"
        f"同时保留音乐课堂、学生互动和原曲重构对比的展示语境。"
    )
