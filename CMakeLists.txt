cmake_minimum_required (VERSION 2.4)
project (Animator)

set(CMAKE_BUILD_TYPE ${ANIMATOR_DEBUG})

set (ANIMATOR_VERSION_MAJOR 0)
set (ANIMATOR_VERSION_MINOR 1)
set (ANIMATOR_VERSION_MICRO 0)

#------------------------------------------------------------
# BUILD SWIG MODULE
#------------------------------------------------------------

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
FIND_PACKAGE(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

set(CMAKE_SWIG_FLAGS "-v")
set_source_files_properties(animator.i PROPERTIES CPLUSPLUS ON)
set_source_files_properties(animator.i PROPERTIES SWIG_FLAGS "-includeall")
swig_add_module(animatorapi python animator.cxx animator.i 
        code/model/layer.cxx 
        code/model/size.cxx)
swig_link_libraries(animatorapi ${PYTHON_LIBRARIES})


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


enable_testing()
add_test(AnimatorRun animator)
set_tests_properties(AnimatorRun
    PROPERTIES PASS_REGULAR_EXPRESSION "Hello, World!")
