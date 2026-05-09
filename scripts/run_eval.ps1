# run_eval.ps1 -- single-command data-collection layer for scout-research (Skill 1).
#
# Runs the seven NBA domain scripts (1, 2, 3, 4, 5, 6, 8 -- Domain 7 has no script)
# against a single player, then reports which JSON outputs were written and
# surfaces any failures so Skill 1 can decide whether to retry, fall back to
# manual lookup, or proceed with partial data.
#
# Usage:
#   .\scripts\run_eval.ps1 "Player Name"
#   .\scripts\run_eval.ps1 "Player Name" -Comp           # also run NBA_Comp_Stats
#   .\scripts\run_eval.ps1 "Player Name" -Playoff        # also run Playoff_Track_Record
#   .\scripts\run_eval.ps1 "Player Name" -Comp -Playoff  # run everything
#   .\scripts\run_eval.ps1 "Player Name" -NoCache        # bypass the league-stats cache
#
# This script is the data-collection layer ONLY. It does not interpret output,
# score sub-domains, or write to raw/ -- that's Skill 1's job downstream.
#
# Exit code 0 = all required scripts produced fresh JSON.
# Exit code 1 = at least one script failed or produced no output.

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Player,

    [switch]$Comp,
    [switch]$Playoff,
    [switch]$NoCache
)

$ErrorActionPreference = 'Continue'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$startTime = Get-Date

if ($NoCache) {
    $env:BBSCOUT_NO_CACHE = '1'
    Write-Host "  (BBSCOUT_NO_CACHE=1 -- bypassing league-stats cache for this run)" -ForegroundColor Yellow
}

# (script-file, output-json) pairs. The seven domain scripts always run.
$domainJobs = @(
    @{ Script = 'Domain_1_Finishing__Stats.py';  Output = 'finishing_output.json'   ; Label = 'Domain 1 - Finishing' },
    @{ Script = 'Domain_2_Shooting__Stats.py';   Output = 'shooting_output.json'    ; Label = 'Domain 2 - Shooting' },
    @{ Script = 'Domain_3_Ball_Skills__Stats.py';Output = 'ball_skills_output.json' ; Label = 'Domain 3 - Ball Skills' },
    @{ Script = 'Domain_4_Playmaking__Stats.py'; Output = 'playmaking_output.json'  ; Label = 'Domain 4 - Playmaking' },
    @{ Script = 'Domain_5_Defense__Stats.py';    Output = 'defense_output.json'     ; Label = 'Domain 5 - Defense' },
    @{ Script = 'Domain_6_Rebounding__Stats.py'; Output = 'rebounding_output.json'  ; Label = 'Domain 6 - Rebounding' },
    @{ Script = 'Domain_8_IQ_Motor__Stats.py';   Output = 'iq_motor_output.json'    ; Label = 'Domain 8 - IQ / Motor' }
)

if ($Playoff) {
    $domainJobs += @{ Script = 'Playoff_Track_Record.py'; Output = 'playoff_track_record_output.json'; Label = 'R13 Playoff Track Record' }
}
if ($Comp) {
    $domainJobs += @{ Script = 'NBA_Comp_Stats.py'; Output = 'comp_stats_output.json'; Label = 'NBA Comp stats' }
}

Write-Host ""
Write-Host "=================================================================="
Write-Host " run_eval.ps1 -- $Player"
Write-Host " started $($startTime.ToString('yyyy-MM-dd HH:mm:ss'))"
Write-Host "=================================================================="
Write-Host ""

$results = @()
$jobIndex = 0
$totalJobs = $domainJobs.Count

foreach ($job in $domainJobs) {
    $jobIndex++
    $scriptPath = Join-Path $scriptDir $job.Script
    $outputPath = Join-Path $scriptDir $job.Output

    Write-Host "[$jobIndex/$totalJobs] $($job.Label) -- running $($job.Script) ..."

    if (-not (Test-Path $scriptPath)) {
        Write-Host "  ERROR: script not found at $scriptPath" -ForegroundColor Red
        $results += [pscustomobject]@{
            Label    = $job.Label
            Script   = $job.Script
            Status   = 'missing-script'
            Duration = 0
        }
        continue
    }

    $jobStart = Get-Date
    Push-Location $scriptDir
    try {
        # python prints UTF-8; force the same on the receiving end so emoji /
        # non-ASCII chars in output don't break the host console.
        $env:PYTHONIOENCODING = 'utf-8'
        & python $job.Script $Player 2>&1 | ForEach-Object { Write-Host "    $_" }
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }
    $jobDuration = (Get-Date) - $jobStart

    $outputFresh = $false
    if (Test-Path $outputPath) {
        $outputMtime = (Get-Item $outputPath).LastWriteTime
        $outputFresh = $outputMtime -ge $startTime
    }

    if ($exitCode -eq 0 -and $outputFresh) {
        $status = 'ok'
        Write-Host "  OK ($([math]::Round($jobDuration.TotalSeconds, 1))s) -> $($job.Output)" -ForegroundColor Green
    }
    elseif ($exitCode -ne 0) {
        $status = "exit-$exitCode"
        Write-Host "  FAIL exit=$exitCode after $([math]::Round($jobDuration.TotalSeconds, 1))s" -ForegroundColor Red
    }
    elseif (-not (Test-Path $outputPath)) {
        $status = 'no-output-file'
        Write-Host "  FAIL no output file produced at $($job.Output)" -ForegroundColor Red
    }
    else {
        $status = 'stale-output'
        Write-Host "  FAIL output file exists but is stale (older than run start)" -ForegroundColor Red
    }

    $results += [pscustomobject]@{
        Label    = $job.Label
        Script   = $job.Script
        Status   = $status
        Duration = [math]::Round($jobDuration.TotalSeconds, 1)
    }
    Write-Host ""
}

$elapsed = (Get-Date) - $startTime
$okCount   = ($results | Where-Object { $_.Status -eq 'ok' }).Count
$failCount = $totalJobs - $okCount

Write-Host "=================================================================="
Write-Host " SUMMARY -- $okCount/$totalJobs ok, $failCount failed"
Write-Host " elapsed $([math]::Round($elapsed.TotalSeconds, 1))s"
Write-Host "=================================================================="
$results | Format-Table -AutoSize

if ($failCount -gt 0) {
    Write-Host ""
    Write-Host "Some scripts failed. Skill 1 should retry the failed ones individually," -ForegroundColor Yellow
    Write-Host "or fall back to manual lookup per SCRIPT-REGISTRY.md." -ForegroundColor Yellow
    exit 1
}

exit 0
