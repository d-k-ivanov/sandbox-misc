set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/3_general_features)
add_executable(structured_bindings "structured_bindings.cpp")
add_executable(structured_bindings_custom "structured_bindings_custom.cpp")
add_executable(init_if_and_switch "init_if_and_switch.cpp")
add_executable(inline_var "inline_var.cpp")
add_executable(lambda_constexpr "lambda_constexpr.cpp")
add_executable(nested_ns "nested_ns.cpp")


if(NOT TARGET 3_general_features)
    add_custom_target(3_general_features)
    add_dependencies(3_general_features structured_bindings)
    add_dependencies(3_general_features structured_bindings_custom)
    add_dependencies(3_general_features init_if_and_switch)
    add_dependencies(3_general_features inline_var)
    add_dependencies(3_general_features lambda_constexpr)
    add_dependencies(3_general_features nested_ns)
endif()

set_target_properties (
    3_general_features
    structured_bindings
    structured_bindings_custom
    init_if_and_switch
    inline_var
    lambda_constexpr
    nested_ns
    PROPERTIES
    FOLDER 3_general_features
)
