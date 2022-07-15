# Реализовать программу подсчета площади, периметра, объема геометрических фигур (треугольник, прямоугольник, квадрат,
# трапеция, окружность). Если одна из фигур не поддерживает вычисление одного из свойств, в программе должно быть
# вызвано исключение с человеко-читабельным сообщением и корректно обработано.

from math import sqrt


class Triangle:

    name = 'Треугольник'

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_area(self):
        half_perimeter = (self.side_1 + self.side_2 + self.side_3) / 2
        area = sqrt(half_perimeter * (half_perimeter - self.side_1) *
                    (half_perimeter - self.side_2) * (half_perimeter - self.side_3))
        return area

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_volume(self):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print('Треугольник является двухмерной фигурой и не имеет объёма')
        return 0


class Rectangle:

    name = 'Прямоугольник'

    def __init__(self, width, height, edge):
        self.width = width
        self.height = height
        self.edge = edge

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_volume(self):
        return self.width * self.height * self.edge


class Square:

    name = 'Квадрат'

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

    def get_volume(self):
        return self.side ** 3


class Trapeze:

    name = 'Трапеция'

    def __init__(self, top_base, bottom_base, lateral_side, height):
        self.top_base = top_base
        self.bottom_base = bottom_base
        self.lateral_side = lateral_side
        self.height = height

    def get_area(self):
        return 0.5 * (self.top_base + self.bottom_base) * self.height

    def get_perimeter(self):
        return self.top_base + self.bottom_base + (2 * self.lateral_side)

    def get_volume(self):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print('Трапеция является двухмерной фигурой и не имеет объёма')
        return 0


class Circle:

    name = 'Круг'

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * self.radius * 3.14

    def get_volume(self):
        return 1.33 * 3.14 * (self.radius ** 3)


figures = [Triangle(4, 5, 6), Rectangle(4, 5, 3), Square(7), Trapeze(5, 7, 6, 4), Circle(8)]

for figure in figures:
    print(f'Площадь фигуры {figure.name} равна:{figure.get_area()}')
    print(f'Периметр фигуры {figure.name} равен:{figure.get_perimeter()}')
    print(f'Объём фигуры {figure.name} равен:{figure.get_volume()}' + '\n')
