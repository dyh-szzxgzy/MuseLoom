import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8080"))
    model_mode: str = os.getenv("MODEL_MODE", "mock")
    deepseek_api_key: str = os.getenv("DEEPSEEK_API_KEY", "")
    coze_api_token: str = os.getenv("COZE_API_TOKEN", "")
    seeddance_api_key: str = os.getenv("SEEDDANCE_API_KEY", "")
    seeddance_api_base_url: str = os.getenv("SEEDDANCE_API_BASE_URL", "")
    seeddance_submit_path: str = os.getenv("SEEDDANCE_SUBMIT_PATH", "/images/generations")
    seeddance_result_path_template: str = os.getenv(
        "SEEDDANCE_RESULT_PATH_TEMPLATE",
        "/images/generations/{task_id}",
    )


settings = Settings()
