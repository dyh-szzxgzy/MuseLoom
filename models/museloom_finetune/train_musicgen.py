import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class MuseLoomTrainingConfig:
    model_name_or_path: str = "facebook/musicgen-melody"
    dataset_name: str = "json"
    dataset_config_name: str | None = None
    train_file: str = "./dataset/train_manifest.jsonl"
    validation_file: str = "./dataset/eval_manifest.jsonl"
    text_column_name: str = "prompt"
    target_audio_column_name: str = "audio"
    instance_prompt: str = "high-school music classroom"
    output_dir: str = "./checkpoints/museloom-lora"
    do_train: bool = True
    do_eval: bool = True
    use_lora: bool = True
    num_train_epochs: int = 4
    learning_rate: float = 2e-4
    per_device_train_batch_size: int = 2
    per_device_eval_batch_size: int = 1
    gradient_accumulation_steps: int = 8
    gradient_checkpointing: bool = True
    logging_steps: int = 1
    eval_steps: int = 25
    max_duration_in_seconds: float = 30.0
    min_duration_in_seconds: float = 1.0
    generation_max_length: int = 400
    guidance_scale: float = 3.0
    fp16: bool = True
    seed: int = 456
    overwrite_output_dir: bool = True
    preprocessing_num_workers: int = 4
    dataloader_num_workers: int = 4
    pad_token_id: int = 2048
    decoder_start_token_id: int = 2048
    report_to: str = "none"


def config_to_cli_args(config: MuseLoomTrainingConfig) -> list[str]:
    config_dict = asdict(config)
    cli_args: list[str] = []
    for key, value in config_dict.items():
        arg_name = f"--{key}"
        if isinstance(value, bool):
            if value:
                cli_args.append(arg_name)
            continue
        if value is None:
            continue
        cli_args.extend([arg_name, str(value)])
    return cli_args


def build_training_command(
    config: MuseLoomTrainingConfig,
    upstream_script: str = "dreambooth_musicgen.py",
) -> str:
    args = config_to_cli_args(config)
    return "python " + " ".join([upstream_script, *args])


def save_config(config: MuseLoomTrainingConfig, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(asdict(config), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare MuseLoom LoRA fine-tuning config for MusicGen."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("./configs/museloom_lora.json"),
        help="Path to a JSON training config.",
    )
    parser.add_argument(
        "--print-command",
        action="store_true",
        help="Print the upstream dreambooth_musicgen.py command.",
    )
    parser.add_argument(
        "--write-config",
        action="store_true",
        help="Write the default config if the target file does not exist.",
    )
    return parser.parse_args()


def load_config(path: Path) -> MuseLoomTrainingConfig:
    if not path.exists():
        return MuseLoomTrainingConfig()
    data = json.loads(path.read_text(encoding="utf-8"))
    return MuseLoomTrainingConfig(**data)


def main() -> None:
    args = parse_args()
    config = load_config(args.config)

    if args.write_config and not args.config.exists():
        save_config(config, args.config)

    command = build_training_command(config)
    payload = {
        "status": "config_ready",
        "config_path": str(args.config),
        "output_dir": config.output_dir,
        "training_command": command,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
