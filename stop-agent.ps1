# Kills any Python process running from the project's venv
$ErrorActionPreference = "SilentlyContinue"
$venvPython = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
$procs = Get-Process | Where-Object { $_.Path -eq (Resolve-Path $venvPython).Path }
if ($procs) {
  $procs | Stop-Process -Force
  Write-Host "Stopped" $procs.Count "agent process(es)."
} else {
  Write-Host "No running agent process found."
}
