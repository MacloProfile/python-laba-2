class Shapes:
    def __init__(self, n_angles, angles, sides):
        self.n_angles = n_angles
        self.angles = angles
        self.sides = sides

        # восстановление углов
        if len(angles) == n_angles - 1:
            self.angles.append((n_angles - 2) * 180 - sum(angles))

        if not self.validate():
            raise ValueError("Invalid shape: check angles and sides.")

    def validate(self):
        if self.n_angles == 0:  # Для круга
            return len(self.sides) == 1 and self.sides[0] > 0

        if len(self.angles) != self.n_angles or len(self.sides) != self.n_angles:
            return False
        if any(angle <= 0 or angle >= 360 for angle in self.angles):
            return False
        if any(side <= 0 for side in self.sides):
            return False
        if self.n_angles > 2 and sum(self.angles) != (self.n_angles - 2) * 180:
            return False
        return True

    def get_perimeter(self):
        return sum(self.sides)

    def get_info(self):
        return {
            "Angles": self.angles,
            "Sides": self.sides,
            "Perimeter": self.get_perimeter(),
        }
