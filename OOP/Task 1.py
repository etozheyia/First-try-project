# Написать методы, производящие следующие операции с векторами: сложение, вычитание, умножение; а также методы,
# осуществляющие проверку на равенство/ не равенство векторов

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.x + other.x, self.y + other.y
        raise NotImplemented('Вектор необходимо сложить с другим вектором')

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.x - other.x, self.y - other.y
        raise NotImplemented('Из вектора необходимо вычесть другой вектор')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.x * other, self.y * other
        raise NotImplemented('Необходимо перемножить вектор на число')

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        raise TypeError('Операнд справа должен иметь тип Vector')
