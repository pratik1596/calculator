import unittest
from Calculator import Calculator
from CSVReader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.object = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.object, Calculator)

    def test_addition_method_calculator(self):
        print("...Starting Addition Testing")
        test_data = CSVReader('./src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.object.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.object.result, int(row['Result']))
        print("Addition Test Completed...")

    def test_subtraction_method_calculator(self):
        print("...Starting Subtraction Testing")
        test_data = CSVReader('./src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.object.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.object.result, int(row['Result']))
        print("Subtraction Test Completed...")

    def test_multiplication_method_calculator(self):
        print("...Starting Multiplication Testing")
        test_data = CSVReader('./src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.object.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.object.result, int(row['Result']))
        print("Multiplication Test Completed...")

    def test_square_method_calculator(self):
        print("...Starting Square Testing")
        test_data = CSVReader('./src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.object.sq(row['Value 1']), int(row['Result']))
            self.assertEqual(self.object.result, int(row['Result']))
        print("Square Test Completed...")

    def test_squareroot_method_calculator(self):
        print("...Starting Square Root Testing")
        test_data = CSVReader('./src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.object.root(row['Value 1']), float(row['Result']))
            self.assertEqual(self.object.result, float(row['Result']))
        print("Square Root Test Completed...")

if __name__ == '__main__':
    unittest.main()
