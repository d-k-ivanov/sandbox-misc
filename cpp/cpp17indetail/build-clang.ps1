#!/usr/bin/env pwsh
${arch} = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]

clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/0_map.exe src/0_quick_start/map.cpp
