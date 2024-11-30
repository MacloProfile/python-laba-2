import math

from src.shapes_sample import Shapes


class Quadrangle(Shapes):
    def __init__(self, angles, sides):
        super().__init__(4, angles, sides)
        self.name = "Quadrangle"

    def get_sq(self):
        try:
            if len(self.sides) == 4:
                a, b, c, d = self.sides

                # Квадрат или прямоугольник
                if all(angle == 90 for angle in self.angles):
                    return a * b

                # Параллелограмм или ромб
                if self.angles[0] == self.angles[2]:
                    height = b * math.sin(math.radians(self.angles[0]))
                    return a * height

                # Трапеция
                if self.angles[0] + self.angles[2] == 180:
                    height = b * math.sin(math.radians(self.angles[0]))
                    return 0.5 * (a + c) * height

            return "Insufficient data for area calculation."
        except Exception as e:
            return f"Error calculating area: {str(e)}"

    def set_angles(self, angles):
        self.angles = angles
        if not self.validate():
            raise ValueError("Invalid angles.")

    def set_sides(self, sides):
        self.sides = sides
        if not self.validate():
            raise ValueError("Invalid sides.")

    def get_info(self):
        area = self.get_sq()
        return {
            "Name": self.name,
            "Angles": self.angles,
            "Sides": self.sides,
            "Perimeter": self.get_perimeter(),
            "Area": area if area else "Not calculable",
        }
