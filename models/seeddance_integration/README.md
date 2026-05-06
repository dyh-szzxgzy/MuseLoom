# SeedDance Integration Module

This folder contains placeholder integration code for visual prompt generation.

## Intended Responsibilities

- Convert music analysis results into visual descriptors.
- Call a visual generation provider in later phases.
- Support classroom comparison between original and regenerated music.

## Generic Diffusion Flow

- Build a text prompt from music style and mood tags
- Submit an image generation task to a diffusion-style API
- Poll the task result endpoint
- Return an image URL or local path for frontend display

## Included Examples

- `request_example.json`
- `response_example.json`
