import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instaniate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(Calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
