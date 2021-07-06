#Static Methods

def addition(value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    return value1 + value2


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, value1, value2):
        self.result = addition(value1, value2)
        return self.result
