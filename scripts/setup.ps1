param([string]$UvPath = "uv")

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$reportDir = Join-Path $projectRoot "work/setup"
$reportPath = Join-Path $reportDir "report.json"
$stage = "preflight"

function Save-SetupStatus([string]$Status) {
    @{status=$Status; stage=$stage; timestamp=[DateTime]::UtcNow.ToString("o")} |
        ConvertTo-Json | Set-Content -LiteralPath $reportPath -Encoding UTF8
}

function Invoke-Uv([string[]]$Arguments) {
    & $script:uvExecutable @Arguments
    if ($LASTEXITCODE -ne 0) { throw "uv failed at $stage (exit $LASTEXITCODE)." }
}

Push-Location $projectRoot
try {
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
    Save-SetupStatus "running"
    if ([Environment]::OSVersion.Platform -ne [PlatformID]::Win32NT) {
        throw "This setup entry point supports Windows only."
    }
    foreach ($name in @("pyproject.toml", "uv.lock", ".python-version")) {
        if (-not (Test-Path -LiteralPath $name -PathType Leaf)) { throw "Missing $name." }
    }
    if ($env:UV_PROJECT_ENVIRONMENT) {
        throw "Unset UV_PROJECT_ENVIRONMENT for this process; STS uses the project's .venv."
    }
    $script:uvExecutable = (Get-Command $UvPath -CommandType Application -ErrorAction Stop).Source
    Invoke-Uv @("--version")
    $stage = "sync"
    Save-SetupStatus "running"
    Invoke-Uv @("sync", "--locked")
    $stage = "initialize"
    Save-SetupStatus "running"
    Invoke-Uv @("run", "--locked", "python", "scripts/init_workspace.py")
    $stage = "verify"
    Save-SetupStatus "running"
    Invoke-Uv @("run", "--locked", "python", "scripts/check_setup.py")
    $stage = "complete"
    Save-SetupStatus "passed"
    Write-Output "STS setup passed. Restart your Agent and open a new session; see guides/getting-started.md."
}
catch {
    if (Test-Path -LiteralPath $reportDir) { Save-SetupStatus "failed" }
    Write-Error $_ -ErrorAction Continue
    exit 1
}
finally { Pop-Location }
