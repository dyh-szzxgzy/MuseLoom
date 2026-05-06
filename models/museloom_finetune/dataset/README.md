# Dataset Layout

Expected dataset structure for future fine-tuning:

- audio files grouped by genre or teaching unit
- metadata file with style, mood, instrument, and difficulty tags
- optional lesson notes for education-specific use cases

## Local Files

- `metadata_example.csv`: source spreadsheet-style metadata
- `train_manifest.jsonl`: normalized training manifest for `datasets`
- `eval_manifest.jsonl`: normalized validation manifest
- `audio/`: local wav or mp3 files referenced by the manifests

## Suggested Prompt Pattern

Use short, structured descriptions centered on:

- style
- mood
- instrument
- teaching topic
