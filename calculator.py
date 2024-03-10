# calculator.py

import math

class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        if value2 != 0:
            return value1 / value2
        else:
            raise ValueError("Cannot divide by zero")
   
    def squareroot(self, value1):
        return math.sqrt(value1)
    

rslt_add = SimpleCalculator().add(5, 3)
rslt_subtract = SimpleCalculator().subtract(10, 4)

print(rslt_add)