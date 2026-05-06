import argparse
from pathlib import Path


def build_inference_snippet(
    repo_id: str,
    prompts: list[str],
    output_dir: str,
    use_cuda: bool = True,
) -> str:
    prompt_lines = ", ".join([repr(prompt) for prompt in prompts])
    device_expr = '"cuda:0" if torch.cuda.device_count() > 0 else "cpu"'
    if not use_cuda:
        device_expr = '"cpu"'

    return f"""from peft import PeftConfig, PeftModel
from transformers import AutoModelForTextToWaveform, AutoProcessor
import torch
import soundfile as sf
from pathlib import Path

device = torch.device({device_expr})
repo_id = "{repo_id}"
config = PeftConfig.from_pretrained(repo_id)
model = AutoModelForTextToWaveform.from_pretrained(
    config.base_model_name_or_path,
    torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
)
model = PeftModel.from_pretrained(model, repo_id).to(device)
processor = AutoProcessor.from_pretrained(repo_id)
inputs = processor(text=[{prompt_lines}], padding=True, return_tensors="pt").to(device)
audio_values = model.generate(**inputs, do_sample=True, guidance_scale=3, max_new_tokens=256)
sampling_rate = model.config.audio_encoder.sampling_rate
audio_values = audio_values.cpu().float().numpy()
output_dir = Path("{output_dir}")
output_dir.mkdir(parents=True, exist_ok=True)
for index, audio_value in enumerate(audio_values):
    sf.write(output_dir / f"musicgen_out_{{index}}.wav", audio_value.T, sampling_rate)
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a MuseLoom MusicGen LoRA inference snippet."
    )
    parser.add_argument(
        "--repo-id",
        default="your-org/museloom-melody-lora",
        help="LoRA adapter repo or local checkpoint path.",
    )
    parser.add_argument(
        "--prompt",
        action="append",
        default=[
            "高中音乐课堂演示用，印象派钢琴片段，情绪平静，旋律细腻",
            "将原始旋律改写为更温暖的室内乐风格",
        ],
        help="Repeat this argument to add multiple prompts.",
    )
    parser.add_argument(
        "--output-dir",
        default="./outputs",
        help="Directory for generated audio outputs.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    snippet = build_inference_snippet(
        repo_id=args.repo_id,
        prompts=args.prompt,
        output_dir=args.output_dir,
    )
    print(snippet)


if __name__ == "__main__":
    main()
