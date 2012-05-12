include(FindBoost)
find_package(Boost 1.49.0 COMPONENTS unit_test_framework)

if(Boost_FOUND)
    message("Boost_LIBRARIES: " ${Boost_LIBRARIES})
    include_directories(${Boost_INCLUDE_DIRS})
    add_executable(layer_test layer_test.cxx)
    target_link_libraries(layer_test ${Boost_LIBRARIES} model_lib)
endif()

#enable_testing()
#add_test(NAME LayerTest COMMAND layer_test)

