import unittest
import sys
import os

from tools import testutils
from tools.testutils import comparator
from layer import *

class TestBitmapLayer(unittest.TestCase):
    def setUp(self):
        self.layer = BitmapLayer('test', 150, 100)

    def assertImageCompare(self, name, image):
        comp = comparator.ImageComparator(name, "png", "_regr_output")
        image.save(comp.result_file)
        self.assertTrue(comp.compare())
        os.system(comp.result_file)

    def test_create_layer(self):
        self.assertEqual((150, 100), self.layer.size)

    @unittest.skip("")
    def test_draw_line(self):
        self.layer.draw_line((0, 0), (150, 100))
        self.assertImageCompare('draw_line', self.layer.render())

    def test_draw_point(self):
        import math
        w, h = self.layer.size
        amplitude = float(h / 2)
        values = [amplitude + amplitude * math.cos((math.pi * 2) / x) for x in range(1, w)]
        for x, y in enumerate(values):
            self.layer.draw_point((x, int(y)))
        self.assertImageCompare('draw_point', self.layer.render())


if __name__ == "__main__":
    def get_tests():
        testcases = []
        for key, value in globals().iteritems():
            if key.startswith('Test'):
                testcases.append(value)
        return testcases
    testutils.run_report(get_tests(), __file__)

