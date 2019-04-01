set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/1_Functions)

file(GLOB_RECURSE SRC
    "max.hpp"
    "main.cpp"
)

source_group("Main" FILES ${SRC})
add_executable(functions ${SRC})

if(NOT TARGET 1_Functions)
    add_custom_target(1_Functions)
    add_dependencies(1_Functions functions)
endif()

set_target_properties (
    1_Functions
    functions
    PROPERTIES
    FOLDER 1_Functions
)
