import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from tools import testutils, testcommon
from tools.testutils import comparator

import canvas

class TestCanvas(unittest.TestCase):
    def assertImageCompare(self, name, image, view=False):
        comp = comparator.ImageComparator(name, "png", "regr_output")
        image.save(comp.result_file)
        self.assertTrue(comp.compare())
        if view:
            os.system(comp.result_file)

    def test_draw_point(self):
        c = canvas.Canvas(100, 100)
        c.get_active_tool().thickness = 20
        c.point(10, 10)
        image = c.render()
        self.assertImageCompare('canvas_point', image)


if __name__ == '__main__':
    testcommon.init_test(__file__)
    testcommon.run_unit_tests(globals()) 

