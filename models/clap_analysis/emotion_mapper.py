def map_features_to_tags(features: dict) -> dict:
    tempo_bpm = features.get("tempo_bpm", 90)
    rms_energy = features.get("rms_energy", 0.2)

    if tempo_bpm < 100 and rms_energy < 0.3:
        mood_tags = ["平静", "温暖", "沉思"]
    else:
        mood_tags = ["激昂", "明亮", "推进感"]

    return {
        "style_tags": ["印象派", "室内乐", "抒情"],
        "mood_tags": mood_tags,
        "teaching_hint": "适合用作课堂中的风格对比素材。",
    }
