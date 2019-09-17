from math import pi


class Cylinder:

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.width = radius*2
        self.area = pi * radius * radius
        self.volume = self.area * height


if __name__ == "__name__":
    x = Cylinder(10, 2)
    print(x.volume)
