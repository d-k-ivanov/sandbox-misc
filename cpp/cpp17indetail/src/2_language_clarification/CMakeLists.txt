set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/2_language_clarification)
add_executable(evaluation_order "evaluation_order.cpp")
add_executable(copy_elision14 "copy_elision.cpp")
#string(REPLACE "/O2" "/O0" CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
set_target_properties(copy_elision14 PROPERTIES CXX_STANDARD 14 CXX_EXTENSIONS OFF CXX_FLAGS -fno-elide-constructors)
add_executable(copy_elision17 "copy_elision.cpp")
add_executable(copy_elision_non_movable "copy_elision_non_movable.cpp")
#add_executable(exceptions "exceptions.cpp")


if(NOT TARGET 2_language_clarification)
    add_custom_target(2_language_clarification)
    add_dependencies(2_language_clarification evaluation_order)
    add_dependencies(2_language_clarification copy_elision14)
    add_dependencies(2_language_clarification copy_elision17)
    add_dependencies(2_language_clarification copy_elision_non_movable)
endif()

set_target_properties (
    2_language_clarification
    evaluation_order
    copy_elision14
    copy_elision17
    copy_elision_non_movable
    PROPERTIES
    FOLDER 2_language_clarification
)
