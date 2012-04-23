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
swig_add_module(animatorapi python ../animator.cxx animator.i 
        ../code/model/layer.cxx 
        ../code/model/size.cxx)
swig_link_libraries(animatorapi ${PYTHON_LIBRARIES})

