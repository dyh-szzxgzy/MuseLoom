from pathlib import Path


def extract_demo_features(audio_path: str) -> dict:
    return {
        "audio_name": Path(audio_path).name,
        "tempo_bpm": 92,
        "spectral_centroid": 2140.5,
        "zero_crossing_rate": 0.087,
        "rms_energy": 0.214,
        "energy_curve": [0.16, 0.24, 0.38, 0.52, 0.66, 0.72],
    }
