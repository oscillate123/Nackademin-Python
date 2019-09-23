"""
1. Write a Python class to convert an integer to a roman numeral.
I, V, X, L, C, D and M
"""
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (self.radius**2)*pi
        return area

    def get_circumference(self):
        circumference = (self.radius*2)*pi
        return circumference


x = Circle(3)
print(x.get_area())
print(x.get_circumference())
