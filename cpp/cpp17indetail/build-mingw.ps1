#!/usr/bin/env pwsh
${arch}    = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]
${libPath} = (Join-Path $PSScriptRoot "lib/${arch}")
${binPath} = (Join-Path $PSScriptRoot "bin")
${includePath} = (Join-Path $PSScriptRoot "include")

g++ --std=c++17 -O3 -DNDEBUG -o ${binPath}/main.exe src/*.cpp -I "${includePath}" -L"${libPath}" -mwindows
