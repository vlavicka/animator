import os
import sys
import unittest

import animatorapi

class TestSwig(unittest.TestCase):
    def test_swig(self):
        self.assertTrue('swigtest' in dir(animatorapi))


class TestSizeClass(unittest.TestCase):
    def test_size_create_default(self):
        size = animatorapi.Size()
        self.assertEqual(0, size.getWidth())
        self.assertEqual(0, size.getHeight())

    def test_size_create_specified(self):
        size = animatorapi.Size(10, 20)
        self.assertEqual(10, size.getWidth())
        self.assertEqual(20, size.getHeight())


class TestAniModelLayer(unittest.TestCase):
    def setUp(self):
        self.layer = animatorapi.LayerBitmap('test')

    def test_create_bitmap_layer(self):
        self.assertEqual(24, self.layer.getBitDepth())
        self.assertEqual('test', self.layer.getName())
        layer = animatorapi.LayerBitmap('test', 100, 200)
        self.assertEqual(100, layer.getSize().getWidth())
        self.assertEqual(200, layer.getSize().getHeight())

    def test_bitmap_layer_dimension(self):
        self.layer.getSize().setWidth(200)
        self.assertEqual(200, self.layer.getSize().getWidth())
        self.layer.getSize().setHeight(400)
        self.assertEqual(400, self.layer.getSize().getHeight())



if __name__ == "__main__":
    def get_tests():
        testcases = []
        for key, value in globals().iteritems():
            if key.startswith('Test'):
                testcases.append(value)
        return testcases
    sys.argv.append('-v')
    unittest.main()

