#------------------------------------------------------------
# BUILD SWIG MODULE
#------------------------------------------------------------

add_definitions(-DUSESWIG)

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
FIND_PACKAGE(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

set(CMAKE_SWIG_FLAGS "-v")
set_source_files_properties(animator.i PROPERTIES CPLUSPLUS ON)
swig_add_module(animatorapi python ../animator.cxx animator.i)
swig_link_libraries(animatorapi ${PYTHON_LIBRARIES} model_lib)

