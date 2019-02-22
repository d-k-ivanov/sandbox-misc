#!/usr/bin/env pwsh
${arch} = (Get-CimInstance Win32_operatingsystem).OSArchitecture.split('-')[0]

New-Item -Path bin/Release/0_quick_start -ItemType Directory -Force
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -target x86_64-pc-windows-msvc -o bin/Release/0_quick_start/map_demo.exe src/0_quick_start/map_demo.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/0_quick_start/print_demo.exe src/0_quick_start/print_demo.cpp

New-Item -Path bin/Release/1_fixes_and_deprecations -ItemType Directory -Force
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/direct_list_initialisation.exe src/1_fixes_and_deprecations/direct_list_initialisation.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/silent_assert.exe              src/1_fixes_and_deprecations/silent_assert.cpp
clang++ --std=c++14 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_14_1.exe        src/1_fixes_and_deprecations/for_range_loop_14_1.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_1.exe        src/1_fixes_and_deprecations/for_range_loop_17_1.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/1_fixes_and_deprecations/for_range_loop_17_2.exe        src/1_fixes_and_deprecations/for_range_loop_17_2.cpp

New-Item -Path bin/Release/2_language_clarification -ItemType Directory -Force
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/2_language_clarification/evaluation_order.exe           src/2_language_clarification/evaluation_order.cpp
clang++ --std=c++14 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/2_language_clarification/copy_elision14.exe             src/2_language_clarification/copy_elision.cpp              -fno-elide-constructors
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/2_language_clarification/copy_elision17.exe             src/2_language_clarification/copy_elision.cpp
# clang++ --std=c++14 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/2_language_clarification/copy_elision_non_movable.exe   src/2_language_clarification/copy_elision_non_movable.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/2_language_clarification/copy_elision_non_movable.exe   src/2_language_clarification/copy_elision_non_movable.cpp

New-Item -Path bin/Release/3_general_features -ItemType Directory -Force
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/structured_bindings.exe              src/3_general_features/structured_bindings.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/structured_bindings_custom.exe       src/3_general_features/structured_bindings_custom.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/init_if_and_switch.exe               src/3_general_features/init_if_and_switch.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/inline_var.exe                       src/3_general_features/inline_var.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/lambda_constexpr.exe                 src/3_general_features/lambda_constexpr.cpp
clang++ --std=c++17 -g -O3 -DNDEBUG -Xclang -flto-visibility-public-std -o bin/Release/3_general_features/nested_ns.exe                        src/3_general_features/nested_ns.cpp

New-Item -Path bin/Release/4_templates -ItemType Directory -Force
