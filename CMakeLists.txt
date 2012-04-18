cmake_minimum_required (VERSION 2.4)
project (Animator)

set (Animator_VERSION_MAJOR 0)
set (Animator_VERSION_MINOR 1)

#------------------------------------------------------------
# BUILD

configure_file (
    "${PROJECT_SOURCE_DIR}/version.h.in"
    "${PROJECT_BINARY_DIR}/version.h")
include_directories("${PROJECT_BINARY_DIR}")

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
FIND_PACKAGE(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

set(CMAKE_SWIG_FLAGS "")
set_source_files_properties(test.i PROPERTIES CPLUSPLUS ON)
set_source_files_properties(test.i PROPERTIES SWIG_FLAGS "-includeall")
swig_add_module(test python test.i test.cxx)
swig_link_libraries(test ${PYTHON_LIBRARIES})

add_executable(test test.cxx src/model/layer.cxx)
