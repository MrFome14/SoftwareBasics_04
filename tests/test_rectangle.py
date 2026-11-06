
import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(10, 0)
        self.assertEqual(result, 0)

    def test_area_one(self):
        result = area(1, 1)
        self.assertEqual(result, 1)

    def test_area_regular(self):
        result = area(4, 6)
        self.assertEqual(result, 24)

    def test_area_float(self):
        result = area(2.5, 3.5)
        self.assertAlmostEqual(result, 8.75)

    def test_perimeter_zero(self):
        result = perimeter(10, 0)
        self.assertEqual(result, 20)

    def test_perimeter_one(self):
        result = perimeter(1, 1)
        self.assertEqual(result, 4)

    def test_perimeter_regular(self):
        result = perimeter(4, 6)
        self.assertEqual(result, 20)

    def test_perimeter_float(self):
        result = perimeter(2.5, 3.5)
        self.assertAlmostEqual(result, 12)
