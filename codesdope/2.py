"""
Create a Temperature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""


class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def c_celsius(self):
        # Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
        celsius = (self.temp-32)/(9/5)
        return celsius

    def c_fahrenheit(self):
        # Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
        fahrenheit = (self.temp*(9/5))+32
        return fahrenheit


x = Temperature(50)
print(x.c_celsius())
print(x.c_fahrenheit())
