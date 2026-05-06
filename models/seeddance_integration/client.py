from dataclasses import dataclass
from time import sleep

import requests


@dataclass
class DiffusionClientConfig:
    api_key: str
    base_url: str
    submit_path: str = "/images/generations"
    result_path_template: str = "/images/generations/{task_id}"
    timeout_seconds: int = 30
    poll_interval_seconds: int = 2
    max_poll_attempts: int = 6
    provider_name: str = "SeedDance 2.0"


def build_headers(config: DiffusionClientConfig) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {config.api_key}",
        "Content-Type": "application/json",
    }


def build_submit_url(config: DiffusionClientConfig) -> str:
    return config.base_url.rstrip("/") + config.submit_path


def build_result_url(config: DiffusionClientConfig, task_id: str) -> str:
    path = config.result_path_template.format(task_id=task_id)
    return config.base_url.rstrip("/") + path


def submit_generation_task(
    prompt: str,
    config: DiffusionClientConfig,
    negative_prompt: str | None = None,
    width: int = 1024,
    height: int = 1024,
    guidance_scale: float = 7.5,
    num_inference_steps: int = 30,
) -> dict:
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt or "",
        "width": width,
        "height": height,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
        "response_format": "url",
    }
    response = requests.post(
        build_submit_url(config),
        headers=build_headers(config),
        json=payload,
        timeout=config.timeout_seconds,
    )
    response.raise_for_status()
    return response.json()


def poll_generation_task(task_id: str, config: DiffusionClientConfig) -> dict:
    last_payload: dict | None = None
    for _ in range(config.max_poll_attempts):
        response = requests.get(
            build_result_url(config, task_id),
            headers=build_headers(config),
            timeout=config.timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
        last_payload = payload
        status = payload.get("status", "").lower()
        if status in {"succeeded", "completed", "finished"}:
            return payload
        if status in {"failed", "error", "cancelled"}:
            return payload
        sleep(config.poll_interval_seconds)

    return last_payload or {"status": "timeout", "task_id": task_id}


def extract_image_result(payload: dict) -> dict:
    data = payload.get("data") or {}
    images = payload.get("images") or data.get("images") or []
    first_image = images[0] if images else {}
    return {
        "status": payload.get("status", "unknown"),
        "task_id": payload.get("task_id") or data.get("task_id"),
        "image_url": first_image.get("url") or payload.get("image_url"),
        "image_path": first_image.get("path") or payload.get("image_path"),
        "raw_payload": payload,
    }


def generate_image(
    prompt: str,
    config: DiffusionClientConfig,
    negative_prompt: str | None = None,
) -> dict:
    submit_payload = submit_generation_task(
        prompt=prompt,
        config=config,
        negative_prompt=negative_prompt,
    )
    task_id = submit_payload.get("task_id") or submit_payload.get("id")
    if not task_id:
        return {
            "status": "submit_unknown",
            "prompt": prompt,
            "provider": config.provider_name,
            "raw_payload": submit_payload,
        }

    result_payload = poll_generation_task(task_id, config)
    result = extract_image_result(result_payload)
    result["provider"] = config.provider_name
    result["prompt"] = prompt
    return result
