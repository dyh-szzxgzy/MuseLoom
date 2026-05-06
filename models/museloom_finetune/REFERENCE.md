# Upstream Reference

MuseLoom fine-tuning is designed around the workflow used by:

- `https://github.com/ylacombe/musicgen-dreamboothing`

## How This Folder Relates To The Upstream Project

- `train_musicgen.py` prepares a MuseLoom-specific config and command line for `dreambooth_musicgen.py`.
- `prepare_dataset.py` converts local CSV metadata into JSONL manifests suitable for `datasets`.
- `infer_musicgen.py` prints a practical LoRA inference snippet for adapted checkpoints.

## Suggested Usage

1. Prepare local audio and metadata under `dataset/`.
2. Run `prepare_dataset.py` to build `train_manifest.jsonl` and `eval_manifest.jsonl`.
3. Place or clone the upstream `dreambooth_musicgen.py` script in a training workspace.
4. Run `train_musicgen.py --print-command` to get a MuseLoom-aligned training command.
5. Use `infer_musicgen.py` with your checkpoint or Hub repo to generate demo outputs.
