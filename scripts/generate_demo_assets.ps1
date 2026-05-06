$projectRoot = Split-Path -Parent $PSScriptRoot

Write-Host "MuseLoom demo asset checklist"
Write-Host ""
Write-Host "Expected source assets:"
Write-Host " - data/samples/sample_audio.wav"
Write-Host " - data/samples/generated_demo.wav"
Write-Host " - data/samples/sample_visual_prompt.txt"
Write-Host ""
Write-Host "Suggested capture outputs:"
Write-Host " - demo/screenshots/homepage.png"
Write-Host " - demo/screenshots/analysis-panel.png"
Write-Host " - demo/screenshots/notebook-proof.png"
Write-Host ""
Write-Host "Project root:" $projectRoot
