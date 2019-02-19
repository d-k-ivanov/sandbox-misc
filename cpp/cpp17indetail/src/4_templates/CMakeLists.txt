set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/4_templates)
add_executable(deduction "deduction.cpp")


if(NOT TARGET 4_templates)
    add_custom_target(4_templates)
    add_dependencies(4_templates deduction)
endif()

set_target_properties (
    4_templates
    deduction
    PROPERTIES
    FOLDER 4_templates
)
