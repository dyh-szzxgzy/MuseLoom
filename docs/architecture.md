# MuseLoom Architecture

## Overview

MuseLoom is organized as a presentation-oriented multi-module project with a clear path toward future execution:

1. `frontend/` handles upload, prompt editing, charts, and playback-oriented presentation.
2. `backend/` exposes unified APIs and coordinates audio analysis, music generation, and visual prompt generation.
3. `models/` stores model-facing scripts, demos, and fine-tuning materials.
4. `demo/` and `docs/` support roadshow storytelling with architecture notes, scripts, and sample assets.

## Primary Flow

1. User uploads a music clip.
2. Backend calls the analysis service to extract tempo, mood, and style tags.
3. User edits prompt tags in the frontend.
4. Backend sends the edited prompt to the music generation service.
5. Visual prompt generation converts the resulting tags into a display-oriented image prompt.
6. Frontend renders analysis cards, spectrum graphics, and output comparisons.

## Current Scaffold Status

- Frontend is scaffolded with mock-driven rendering.
- Backend exposes mock APIs for analysis, generation, and visualization.
- Model folders contain placeholder scripts and notebooks for demo and future implementation.
- Training and inference are currently demonstration-oriented and not production-complete.
