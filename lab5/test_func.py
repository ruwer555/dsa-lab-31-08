import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):

    # ПОЗИТИВНЫЕ ТЕСТЫ 
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles_2(self):
        self.assertEqual(get_triangle_type(5, 5, 8), "isosceles")

    def test_isosceles_3(self):
        self.assertEqual(get_triangle_type(6, 7, 6), "isosceles")

    def test_nonequilateral_1(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_nonequilateral_2(self):
        self.assertEqual(get_triangle_type(10, 11, 12), "nonequilateral")

    def test_float_sides(self):
        self.assertEqual(get_triangle_type(0.5, 0.6, 0.7), "nonequilateral")

    # НЕГАТИВНЫЕ ТЕСТЫ 
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 5, 5)

    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 3, 4)

    def test_triangle_inequality_1(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)

    def test_triangle_inequality_2(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 2, 3)

    def test_invalid_type_str(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 5, 5)

    def test_invalid_type_none(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(None, 4, 5)
