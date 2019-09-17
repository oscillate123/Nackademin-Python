from random import randint
from forelasning_10.uppgift_1.cylinder import Cylinder


class Stack:

    def __init__(self, n_cylinders):
        self.cylinders = [(Cylinder(randint(0, 10), randint(0, 5))) for _ in range(n_cylinders)]

    def get_stack_height(self):
        height = sum([cylinder.height for cylinder in self.cylinders])
        return height
        # TODO: Return the height of the stacked cylinders.

    def get_stack_width(self):
        width = max([cylinder.width for cylinder in self.cylinders])
        return width
        # TODO: Return the width of the tower.

    def get_stack_volume(self):
        volume = sum([cylinder.volume for cylinder in self.cylinders])
        return volume
        # TODO: Return the volume of the tower.


if __name__ == "__main__":
    print(" x ")
