import unittest
import calc

def add(a, b):
    return a + b

def testadd():
    assert 1 + 1 == 2

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_calc_add(self):
        self.assertEqual(calc.Calculator.add(self, 2, 1), 3)

    def test_calc_integration(self):
        self.assertEqual((calc.Calculator.add(self, 2, 1)+calc.Calculator.subtract(self, 5, 2)), 6)