#include <string>
#include "../code/model/layer.h"
#define BOOST_TEST_MAIN
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_CASE (my_test)
{
    LayerBitmap layer = LayerBitmap("test");
    BOOST_CHECK(layer.getName() == "test");
}
