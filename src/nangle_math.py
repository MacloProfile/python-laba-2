import math

from src.shapes_sample import Shapes


class Nangle(Shapes):
    def __init__(self, n_angles, angles, sides):
        super().__init__(n_angles, angles, sides)
        self.name = f"{n_angles}-gon"

        # восстановить недостающий угол
        if len(self.angles) == self.n_angles - 1:
            missing_angle = (self.n_angles - 2) * 180 - sum(self.angles)
            if 0 < missing_angle < 360:
                self.angles.append(missing_angle)
            else:
                raise ValueError("Invalid angle configuration.")

    def get_sq(self):
        if len(self.sides) != self.n_angles or len(self.angles) != self.n_angles:
            return "Insufficient data to calculate area."

        x, y = [0], [0]
        angle_sum = 0

        for i in range(self.n_angles):
            angle_sum += self.angles[i]
            x.append(x[-1] + self.sides[i] * math.cos(math.radians(angle_sum)))
            y.append(y[-1] + self.sides[i] * math.sin(math.radians(angle_sum)))

        area = 0
        for i in range(self.n_angles):
            area += x[i] * y[i + 1] - x[i + 1] * y[i]
        area = abs(area) / 2

        return area

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