# Workflow Explanation

## Design Goal

The workflow is designed to mirror the `听 / 创 / 赏` teaching loop described in the project README while also looking like a realistic orchestrated AI pipeline.

## Node Responsibilities

1. `start`
   Collect demo inputs such as the source audio path and classroom context.

2. `analyze_audio`
   Extract style, mood, tempo, and teaching hints from the original music clip.

3. `revise_prompt`
   Convert analysis output into a classroom-friendly generation recipe and user-editable prompt tags.

4. `generate_music`
   Produce the transformed music output while preserving the original melodic structure.

5. `generate_visual_prompt`
   Build a multimodal appreciation prompt aligned with the transformed music.

6. `end`
   Aggregate outputs for frontend display or roadshow demonstration.

## Why It Is More Credible

- Includes explicit inputs and outputs
- Includes a condition or validation stage
- Shows how analysis feeds both generation and appreciation
- Matches the backend demo API shape
- Mirrors a realistic adapter pattern for LLM and multimodal providers
