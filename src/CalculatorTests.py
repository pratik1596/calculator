import unittest
from Calculator import Calculator
from CSVReader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.object = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.object, Calculator)

    def test_addition_method_calculator(self):
        print("Testing Addition")
        test_data = CSVReader('./src/Unit Test Addition.csv').data
        for row in test_data:
            a = row['Value 1']
            b = row['Value 2']
            real_result = int(row['Result'])
            self.assertEqual(self.object.add(a, b), real_result)
            self.assertEqual(self.object.result, real_result)

    def test_subtraction_method_calculator(self):
        print("Testing Subtraction")
        test_data = CSVReader('./src/Unit Test Subtraction.csv').data
        for row in test_data:
            a = row['Value 1']
            b = row['Value 2']
            real_result = int(row['Result'])
            self.assertEqual(self.object.sub(a, b), real_result)
            self.assertEqual(self.object.result, real_result)

if __name__ == '__main__':
    unittest.main()
