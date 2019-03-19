Get-Childitem ./1-hello-world | ForEach-Object {
    rustc --out-dir ./bin/1-hello-world $_.FullName
}
