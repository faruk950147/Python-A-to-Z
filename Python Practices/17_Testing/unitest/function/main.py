import unittest
from test import add, sub, mul, div, mod

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)
    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)
    def test_div(self):
        self.assertEqual(div(1, 2), 0.5)
    def test_mod(self):
        self.assertEqual(mod(1, 2), 1)

if __name__ == '__main__':
    unittest.main()