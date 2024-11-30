from src.circle_math import Circle
from src.nangle_math import Nangle
from src.quadrangle_math import Quadrangle
from src.triangle_math import Triangle


def main():
    circle = Circle(10)
    print(circle.get_info())

    triangle = Triangle([60, 60, 60], [10, 10, 10])
    print(triangle.get_info())

    quadrangle = Quadrangle([90, 90, 90, 90], [10, 20, 10, 20])
    print(quadrangle.get_info())

    pentagon = Nangle(5, [108, 108, 108, 108], [10, 10, 10, 10, 10])
    print(pentagon.get_info())


if __name__ == "__main__":
    main()
