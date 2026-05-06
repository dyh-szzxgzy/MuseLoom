# Backend Module

This backend provides a mock-oriented API scaffold for the MuseLoom roadshow project.

## Endpoints

- `POST /api/analyze`
- `POST /api/generate`
- `POST /api/visualize`
- `POST /api/demo-flow`

## Current Design

- Individual services model the `听 / 创 / 赏` flow
- `orchestrator.py` combines analysis, generation, and visual prompt creation
- Responses are demo-oriented and return structured mock payloads
