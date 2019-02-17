set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/4_templates)
# add_executable(structured_bindings "structured_bindings.cpp")


if(NOT TARGET 4_templates)
    add_custom_target(4_templates)
    # add_dependencies(4_templates nested_ns)
endif()

set_target_properties (
    4_templates
    PROPERTIES
    FOLDER 4_templates
)
