import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_one(self):
        result = area(1)
        self.assertAlmostEqual(result, 3.141592653589793)

    def test_area_five(self):
        result = area(5)
        self.assertAlmostEqual(result, 78.53981633974483)
    
    def test_area_float(self):
        result = area(2.5)
        self.assertAlmostEqual(result, 19.634954084936208)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_one(self):
        result = perimeter(1)
        self.assertAlmostEqual(result, 6.283185307179586)

    def test_perimeter_four(self):
        result = perimeter(4)
        self.assertAlmostEqual(result, 25.132741228718345)

    def test_perimeter_float(self):
        result = area(3.5)
        self.assertAlmostEqual(result, 38.48451000647496)