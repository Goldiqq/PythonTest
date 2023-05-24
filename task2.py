import unittest
import math
#Выполнила Макаренко Александра Александровна, группа 44-22-120, вариант №18
def calc(x):
    if x > 1:
        y = math.sin(math.sqrt(x))
    else:
        y = math.cos(x**2)
    print("Значение y =", y)

class TestCalculateY(unittest.TestCase):
    def test_x_less_than_1(self):
        x = 0
        expected_y = math.cos(x**2)
        self.assertAlmostEqual(calc(x), expected_y, places=5)

    def test_x_greater_than_1(self):
        x = 2
        expected_y = math.sin(math.sqrt(x))
        self.assertAlmostEqual(calc(x), expected_y, places=5)

    def test_x_equal_1(self):
        x = 1
        expected_y = y = math.cos(x**2)
        self.assertAlmostEqual(calc(x), expected_y, places=5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calc("invalid_input")
