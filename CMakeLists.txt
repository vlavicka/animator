cmake_minimum_required (VERSION 2.4)
project (Animator)

set(CMAKE_BUILD_TYPE ${ANIMATOR_DEBUG})

set (ANIMATOR_VERSION_MAJOR 0)
set (ANIMATOR_VERSION_MINOR 1)
set (ANIMATOR_VERSION_MICRO 0)

add_subdirectory("${PROJECT_SOURCE_DIR}/swig")
add_subdirectory("${PROJECT_SOURCE_DIR}/code/model")

#------------------------------------------------------------
# BUILD
#------------------------------------------------------------

configure_file (
    "${PROJECT_SOURCE_DIR}/version.h.in"
    "${PROJECT_BINARY_DIR}/version.h")
include_directories("${PROJECT_BINARY_DIR}")

add_library(Model code/model/layer.cxx code/model/size.cxx)
add_executable(animator animator.cxx)
target_link_libraries(animator Model)


#------------------------------------------------------------
# TESTING
#------------------------------------------------------------


#enable_testing()
add_test(AnimatorRun animator)
set_tests_properties(AnimatorRun PROPERTIES PASS_REGULAR_EXPRESSION "Hello, World!")
