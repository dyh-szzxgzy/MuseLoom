# MuseLoom Fine-tuning Module

This module adapts the project plan in `README.md` to a practical MusicGen fine-tuning scaffold.

## Design Reference

The fine-tuning flow is modeled after the public `ylacombe/musicgen-dreamboothing` project:

- LoRA-based lightweight fine-tuning
- `datasets`-driven dataset loading
- JSON config driven training
- optional melody-guided generation with `facebook/musicgen-melody`

## Local Structure

- `train_musicgen.py`: build and print a ready-to-run training command
- `infer_musicgen.py`: LoRA inference helper for local or Hub checkpoints
- `prepare_dataset.py`: convert local metadata into a normalized manifest
- `configs/museloom_lora.json`: starter config aligned with the current project README
- `dataset/metadata_example.csv`: sample teaching-oriented music metadata

## Notes

- This repository does not vendor the upstream training script.
- The current code prepares MuseLoom-specific configs and commands around that workflow.
- Replace placeholder paths with real local audio or Hugging Face datasets before actual training.
