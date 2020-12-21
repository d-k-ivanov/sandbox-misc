$branch      = "dev/r12_3/divanov/TEST-Task"
# $branch      = "dev/main/divanov/TEST-Task"
# $branch      = "dev/abrakadabra/divanov/TEST-Task"
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
    Write-Output "Unsupported branch. We run SonarCloud for dev/main and dev/rXX_X"
}

Write-Host "${branch}" -ForegroundColor Green
Write-Host "${target}" -ForegroundColor Green
