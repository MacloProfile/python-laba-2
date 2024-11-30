import math

from src.shapes_sample import Shapes


class Circle(Shapes):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Invalid radius.")
        super().__init__(0, [], [radius])
        self.name = "Circle"

    def get_sq(self):
        return math.pi * self.sides[0] ** 2

    def get_info(self):
        return {
            "Name": self.name,
            "Radius": self.sides[0],
            "Perimeter (Circumference)": 2 * math.pi * self.sides[0],
            "Area": self.get_sq(),
        }