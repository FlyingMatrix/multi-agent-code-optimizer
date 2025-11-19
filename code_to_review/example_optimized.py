import math

def factorial(value):
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif value == 0 or value == 1:
        return 1
    else:
        return math.factorial(value)