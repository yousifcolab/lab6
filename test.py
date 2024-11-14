# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_calc(self):
        # Test addition functionality
        result = self.calc.calc(5)
        self.assertEqual(result, 78.5)
        
        result = self.calc.calc(4)
        self.assertEqual(result, 50.24)
        
        result = self.calc.calc(2)
        self.assertEqual(result, 12.56)

if __name__ == '__main__':
    unittest.main()