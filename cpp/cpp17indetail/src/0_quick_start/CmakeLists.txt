set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/0_quick_start)

file(GLOB_RECURSE SRC_MAP
    "map_demo.cpp"
)

source_group("Map" FILES ${SRC_MAP})
add_executable(map_demo ${SRC_MAP})

file(GLOB_RECURSE SRC_PRINT
    "print_demo.cpp"
)

source_group("Print" FILES ${SRC_PRINT})
add_executable(print_demo ${SRC_PRINT})

if(NOT TARGET 0_quick_start)
    add_custom_target(0_quick_start)
    add_dependencies(0_quick_start map_demo)
    add_dependencies(0_quick_start print_demo)
endif()

set_target_properties (
    0_quick_start
    map_demo
    print_demo
    PROPERTIES
    FOLDER 0_quick_start
)
