#!/usr/bin/env pwsh
${arch} = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]

New-Item -Path bin/Release/0_quick_start -ItemType Directory -Force
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/0_quick_start/map_demo.exe   src/0_quick_start/map_demo.cpp
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/0_quick_start/print_demo.exe src/0_quick_start/print_demo.cpp

New-Item -Path bin/Release/1_fixes_and_deprecations -ItemType Directory -Force
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/direct-list-initialisation.exe src/1_fixes_and_deprecations/direct-list-initialisation.cpp
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/silent_assert.exe              src/1_fixes_and_deprecations/silent_assert.cpp
clang --std=c++14 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_14_1.exe        src/1_fixes_and_deprecations/for_range_loop_14_1.cpp
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_1.exe        src/1_fixes_and_deprecations/for_range_loop_17_1.cpp
clang --std=c++17 -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_2.exe        src/1_fixes_and_deprecations/for_range_loop_17_2.cpp
