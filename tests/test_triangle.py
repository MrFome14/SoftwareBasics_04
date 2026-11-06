
import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(0, 5)
        self.assertEqual(result, 0)

    def test_area_one(self):
        result = area(1, 1)
        self.assertAlmostEqual(result, 0.5)

    def test_area_regular(self):
        result = area(6, 4)
        self.assertEqual(result, 12)

    def test_area_float(self):
        result = area(2.5, 3.5)
        self.assertAlmostEqual(result, 4.375)

    def test_perimeter_zero(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    def test_perimeter_one(self):
        result = perimeter(1, 1, 1)
        self.assertEqual(result, 3)

    def test_perimeter_regular(self):
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)

    def test_perimeter_float(self):
        result = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(result, 10.5)
