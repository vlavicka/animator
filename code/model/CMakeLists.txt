add_library(layer_test_lib size.cxx)
add_executable(layer_test layer.cxx)
target_link_libraries(layer_test layer_test_lib)

#enable_testing()

add_test(LayerTest layer_test)
set_tests_properties(LayerTest PROPERTIES PASS_REGULAR_EXPRESSION "Name = test1; size = 0, 0")
set_tests_properties(LayerTest PROPERTIES PASS_REGULAR_EXPRESSION "Name = test2; size = 100, 200")
