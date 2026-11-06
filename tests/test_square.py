
import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_one(self):
        result = area(1)
        self.assertEqual(result, 1)

    def test_area_five(self):
        result = area(5)
        self.assertEqual(result, 25)

    def test_area_float(self):
        result = area(2.5)
        self.assertAlmostEqual(result, 6.25)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_one(self):
        result = perimeter(1)
        self.assertEqual(result, 4)

    def test_perimeter_five(self):
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_perimeter_float(self):
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 10)
