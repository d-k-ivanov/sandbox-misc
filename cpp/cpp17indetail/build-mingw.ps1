#!/usr/bin/env pwsh
${arch} = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]

New-Item -Path bin/Release/0_quick_start -ItemType Directory -Force
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/0_quick_start/map_demo.exe                              src/0_quick_start/map_demo.cpp                              -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/0_quick_start/print_demo.exe                            src/0_quick_start/print_demo.cpp                            -mconsole -lgdi32

New-Item -Path bin/Release/1_fixes_and_deprecations -ItemType Directory -Force
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/1_fixes_and_deprecations/direct_list_initialisation.exe src/1_fixes_and_deprecations/direct_list_initialisation.cpp -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/1_fixes_and_deprecations/silent_assert.exe              src/1_fixes_and_deprecations/silent_assert.cpp              -mconsole -lgdi32
g++ --std=c++14 -O3 -DNDEBUG -s -o bin/Release/1_fixes_and_deprecations/for_range_loop_14_1.exe        src/1_fixes_and_deprecations/for_range_loop_14_1.cpp        -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_1.exe        src/1_fixes_and_deprecations/for_range_loop_17_1.cpp        -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_2.exe        src/1_fixes_and_deprecations/for_range_loop_17_2.cpp        -mconsole -lgdi32

New-Item -Path bin/Release/2_language_clarification -ItemType Directory -Force
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/2_language_clarification/evaluation_order.exe           src/2_language_clarification/evaluation_order.cpp           -mconsole -lgdi32
g++ --std=c++14 -O3 -DNDEBUG -s -o bin/Release/2_language_clarification/copy_elision14.exe             src/2_language_clarification/copy_elision.cpp               -mconsole -lgdi32 -fno-elide-constructors
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/2_language_clarification/copy_elision17.exe             src/2_language_clarification/copy_elision.cpp               -mconsole -lgdi32
#g++ --std=c++14 -O3 -DNDEBUG -s -o bin/Release/2_language_clarification/copy_elision_non_movable.exe   src/2_language_clarification/copy_elision_non_movable.cpp   -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/2_language_clarification/copy_elision_non_movable.exe   src/2_language_clarification/copy_elision_non_movable.cpp   -mconsole -lgdi32

New-Item -Path bin/Release/3_general_features -ItemType Directory -Force
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/3_general_features/structured_bindings.exe              src/3_general_features/structured_bindings.cpp              -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/3_general_features/structured_bindings_custom.exe       src/3_general_features/structured_bindings_custom.cpp       -mconsole -lgdi32
g++ --std=c++17 -O3 -DNDEBUG -s -o bin/Release/3_general_features/init_if_and_switch.exe               src/3_general_features/init_if_and_switch.cpp               -mconsole -lgdi32
