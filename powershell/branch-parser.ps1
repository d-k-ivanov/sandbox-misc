$branches = @(
    "dev/r12_3/divanov/TEST-Task"
    "dev/releases/r12_3/divanov/TEST-Task"
    "dev/dev/r12_3/divanov/TEST-Task"
    "dev/main/divanov/TEST-Task"
    "dev/main/divanov/divanov/TEST-Task"
    "dev/abrakadabra/divanov/TEST-Task"
    "abrakadabra/divanov/TEST-Task"
    "dev"
)

foreach ($branch in $branches)
{
    Write-Host "Branch: ${branch}" -ForegroundColor Green

    $targetBranch = ($branch -split '/')[1]
    $checkIsDev = ($branch -split '/')[0]
    $target      = "main"

    if ($checkIsDev -eq 'dev') {
        if ($targetBranch -eq 'main')
        {
            $target = "main"
        }
        elseif  ($targetBranch -match  "r\d{1,2}_\d{1}" )
        {
            $target = "releases/$targetBranch"
        }
    }
    else
    {
        Write-Host "`tUnsupported branch. We run SonarCloud for dev/main and dev/rXX_X"  -ForegroundColor Red
    }

    Write-Host "Target: ${target}" -ForegroundColor Green
    Write-Host ""
}
