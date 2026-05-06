# Image Generation Flow

## Purpose

This document describes the generic diffusion-based image generation flow used for the MuseLoom `赏` stage.

## Runtime Modes

- `MODEL_MODE="mock"`: return a prompt and placeholder image path
- non-mock mode with API settings: submit a generation task and poll for image output

## Required Variables

- `SEEDDANCE_API_KEY`
- `SEEDDANCE_API_BASE_URL`
- `SEEDDANCE_SUBMIT_PATH`
- `SEEDDANCE_RESULT_PATH_TEMPLATE`

## Generic Request Pattern

1. Build prompt from style tags, mood tags, and teaching focus
2. `POST` to the submit endpoint
3. Extract `task_id`
4. `GET` the result endpoint until completion
5. Return image URL or local path
