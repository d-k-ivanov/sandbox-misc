set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/1_fixes_and_deprecations)
add_executable(direct_list_initialisation "direct_list_initialisation.cpp")
add_executable(silent_assert "silent_assert.cpp")
add_executable(for_range_loop_14_1 "for_range_loop_14_1.cpp")
add_executable(for_range_loop_17_1 "for_range_loop_17_1.cpp")
add_executable(for_range_loop_17_2 "for_range_loop_17_2.cpp")
add_executable(for_range_loop_17_3 "for_range_loop_17_3.cpp")
add_executable(for_loop_examples "for_loop_examples.cpp")

if(NOT TARGET 1_fixes_and_deprecations)
    add_custom_target(1_fixes_and_deprecations)
    add_dependencies(1_fixes_and_deprecations direct_list_initialisation)
    add_dependencies(1_fixes_and_deprecations silent_assert)
    add_dependencies(1_fixes_and_deprecations for_range_loop_14_1)
    add_dependencies(1_fixes_and_deprecations for_range_loop_17_1)
    add_dependencies(1_fixes_and_deprecations for_range_loop_17_2)
    add_dependencies(1_fixes_and_deprecations for_range_loop_17_3)
    add_dependencies(1_fixes_and_deprecations for_loop_examples)
endif()

set_target_properties (
    1_fixes_and_deprecations
    direct_list_initialisation
    silent_assert
    for_range_loop_14_1
    for_range_loop_17_1
    for_range_loop_17_2
    for_range_loop_17_3
    for_loop_examples
    PROPERTIES
    FOLDER 1_fixes_and_deprecations
)
