#!/usr/bin/env pwsh
${arch}        = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]
${libPath}     = (Join-Path $PSScriptRoot "lib/${arch}")
${binPath}     = (Join-Path $PSScriptRoot "bin")
${includePath} = (Join-Path $PSScriptRoot "include")

clang --std=c++17 -O3 -DNDEBUG        `
  -Xclang -flto-visibility-public-std `
  -o ${binPath}/main.exe   `
  -I "${includePath}" -L"${libPath}"  `
  src/*.cpp
