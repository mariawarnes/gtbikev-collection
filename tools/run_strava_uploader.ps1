param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$UploaderArguments
)

$ErrorActionPreference = "Stop"
$ToolDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$VirtualEnvironment = Join-Path $ToolDirectory ".venv"
$Python = Join-Path $VirtualEnvironment "Scripts\python.exe"

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    throw "Python was not found. Install Python 3 from https://www.python.org/downloads/windows/ and enable the Python launcher."
}

if (-not (Test-Path -LiteralPath $Python)) {
    Write-Host "Creating the Strava uploader environment..."
    & py -3 -m venv $VirtualEnvironment
    & $Python -m pip install --disable-pip-version-check -r (Join-Path $ToolDirectory "requirements.txt")
}

& $Python (Join-Path $ToolDirectory "strava_uploader.py") @UploaderArguments
exit $LASTEXITCODE
