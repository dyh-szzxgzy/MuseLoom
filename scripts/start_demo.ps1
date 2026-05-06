$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$backendPath = Join-Path $projectRoot "backend"
$frontendPath = Join-Path $projectRoot "frontend"

Write-Host "MuseLoom demo scaffold"
Write-Host "Project root:" $projectRoot
Write-Host ""
Write-Host "Recommended startup order:"
Write-Host "1. Create and activate a Python virtual environment."
Write-Host "2. Install dependencies from requirements.txt."
Write-Host "3. Start the backend with:"
Write-Host "   uvicorn backend.api_server:app --host 0.0.0.0 --port 8080"
Write-Host "4. Open frontend/index.html in a browser."
Write-Host ""
Write-Host "Backend path:" $backendPath
Write-Host "Frontend path:" $frontendPath
