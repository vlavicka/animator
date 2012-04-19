import os
import sys
import unittest

import animatorapi

class TestSwig(unittest.TestCase):
    def test_swig(self):
        self.assertTrue('swigtest' in dir(animatorapi))

class TestAniModelLayer(unittest.TestCase):
    def test_layer_numer(self):
        layer = animatorapi.LayerBase(1)
        self.assertEqual(1, layer.number)

    def test_bitmap_layer(self):
        layer = animatorapi.LayerBitmap(1)
        self.assertEqual(1, layer.number)
        self.assertEqual(24, layer.bitDepth)


if __name__ == "__main__":
    def get_tests():
        testcases = []
        for key, value in globals().iteritems():
            if key.startswith('Test'):
                testcases.append(value)
        return testcases
    sys.argv.append('-v')
    unittest.main()

