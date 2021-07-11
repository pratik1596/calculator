def division(value1, value2):
    try:
        value1 = float(value1)
        value2 = float(value2)
        return float(value2 / value1)
    except:
        print("Division by zero not possible")