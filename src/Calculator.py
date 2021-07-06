#Static Methods

def addition(value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    return value1 + value2

def subtraction(value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    return value1 - value2

def multiplication(value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    return value1 * value2

def division(value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    return float(value2 / value1)

def square(value1):
    value1 = int(value1)
    return int(value1 * value1)

def sroot(value1):
    value1 = int(value1)
    return float(value1 ** 0.5)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, value1, value2):
        self.result = addition(value1, value2)
        return self.result

    def sub(self, value1, value2):
        self.result = subtraction(value1, value2)
        return self.result

    def mul(self, value1, value2):
        self.result = multiplication(value1, value2)
        return self.result

    def div(self, value1, value2):
        self.result = division(value1, value2)
        return self.result

    def sq(self, value1):
        self.result = square(value1)
        return self.result

    def root(self, value1):
        self.result = sroot(value1)
        return self.result
