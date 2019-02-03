#!/usr/bin/env pwsh
$old_dir = Get-Location

${arch}    = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]
${libPath} = (Join-Path $PSScriptRoot "lib/${arch}")
${binPath} = (Join-Path $PSScriptRoot "bin")

CreateAndSet-Directory build

# Generate
# cmake ..
# cmake -G "MinGW Makefiles" .. -DCMAKE_C_COMPILER=gcc
# cmake -G "Visual Studio 15 2017" ..
cmake -G "Visual Studio 15 2017 Win64" ..

# Build
# cmake --build .
cmake --build . --config "Release"

# Cleanup
Set-Location $old_dir
Remove-Item -Recurse -Force ./build
