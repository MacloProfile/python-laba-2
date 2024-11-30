import math

from src.shapes_sample import Shapes


class Triangle(Shapes):
    def __init__(self, angles, sides):
        super().__init__(3, angles, sides)
        self.name = "Triangle"

    def get_sq(self):
        a, b, c = self.sides
        s = self.get_perimeter() / 2

        try:
            # Формула Герона
            heron_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

            # Формула через угол
            angle_rad = math.radians(self.angles[0])
            angle_area = 0.5 * a * b * math.sin(angle_rad)

            # Через высоту
            h = (2 * heron_area) / c
            height_area = 0.5 * c * h

            return {
                "Heron": heron_area,
                "By Angle": angle_area,
                "By Height": height_area,
            }
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
        return {
            "Name": self.name,
            "Angles": self.angles,
            "Sides": self.sides,
            "Perimeter": self.get_perimeter(),
            "Area": self.get_sq(),
        }