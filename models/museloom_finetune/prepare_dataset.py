import argparse
import csv
import json
from pathlib import Path


def build_prompt(row: dict[str, str]) -> str:
    parts = [
        row.get("style", "").strip(),
        row.get("mood", "").strip(),
        row.get("instrument", "").strip(),
        row.get("teaching_topic", "").strip(),
    ]
    filtered = [part for part in parts if part]
    return "，".join(filtered)


def normalize_audio_path(audio_root: Path, audio_file: str) -> str:
    return str((audio_root / audio_file).resolve())


def convert_csv_to_jsonl(
    csv_path: Path,
    audio_root: Path,
    output_path: Path,
) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with csv_path.open("r", encoding="utf-8-sig", newline="") as source, output_path.open(
        "w",
        encoding="utf-8",
    ) as target:
        reader = csv.DictReader(source)
        for row in reader:
            record = {
                "audio": normalize_audio_path(audio_root, row["audio_file"]),
                "prompt": build_prompt(row),
                "style": row.get("style", ""),
                "mood": row.get("mood", ""),
                "instrument": row.get("instrument", ""),
                "teaching_topic": row.get("teaching_topic", ""),
            }
            target.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert MuseLoom CSV metadata into jsonl manifests for MusicGen training."
    )
    parser.add_argument(
        "--csv-path",
        type=Path,
        default=Path("./dataset/metadata_example.csv"),
    )
    parser.add_argument(
        "--audio-root",
        type=Path,
        default=Path("./dataset/audio"),
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("./dataset/train_manifest.jsonl"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = convert_csv_to_jsonl(args.csv_path, args.audio_root, args.output_path)
    payload = {
        "status": "manifest_ready",
        "records": count,
        "output_path": str(args.output_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
