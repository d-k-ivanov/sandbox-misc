#!/usr/bin/env pwsh
${arch} = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]

g++ --std=c++17 -O3 -DNDEBUG -s -o bin/0_map.exe src/0_quick_start/map.cpp -mconsole -lgdi32
