# calculator.py

import math

class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")
   
    def calculate_square_root(self, x):
        return math.sqrt(x)
