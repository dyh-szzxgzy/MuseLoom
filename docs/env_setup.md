# Environment Setup

## Required Variables

- `DEEPSEEK_API_KEY`
- `COZE_API_TOKEN`
- `SEEDDANCE_API_KEY`
- `MODEL_MODE`
- `API_HOST`
- `API_PORT`

## Suggested Local Values

```env
DEEPSEEK_API_KEY="your_deepseek_v4_api_key"
COZE_API_TOKEN="your_coze_token"
SEEDDANCE_API_KEY="your_seeddance_api_key"
MODEL_MODE="mock"
API_HOST="0.0.0.0"
API_PORT="8080"
```

## Notes

- Keep `MODEL_MODE="mock"` for roadshow demonstrations when live APIs are unavailable.
- Replace keys only when integrating real external services.
