"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты:
 три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и
 периметра). При потребности создавать все необходимые методы не описанные в задании.

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass

class Circle(Figure):
    def __init__(self, coo_x, coo_y, r):
        self.coo_x = coo_x
        self.coo_y = coo_y
        self.r = r

    def len_of_circle(self):
        len = 2*3,14*self.r
        return len

    def sqr_of_circle(self):
        sqr = 3,14*self.r**2
        return sqr

class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def p_of_triangle(self):
        a = (((self.x1 - self.x2) ** 2) + ((self.y1 - self.y2) ** 2)) ** 0,5
        b = (((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2)) ** 0,5
        c = (((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2)) ** 0,5
        perimetr = a + b + c
        return perimetr

    def sqr_of_triangle(self):
        a = (((self.x1 - self.x2)**2) + ((self.y1 - self.y2)**2))**0,5
        b = (((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2)) ** 0,5
        c = (((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2)) ** 0, 5
        p = 0,5*(a+b+c)
        sqr_trl = p*(p - a)(p - b)(p - c)
        return sqr_trl

class Square(Figure):
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2

    def perim_square(self):
        side = (((self.a1 - self.a2) ** 2) + ((self.b1 - self.b2) ** 2)) ** 0,5
        perim = 4*side
        return perim

    def sqr_square(self):
        side = (((self.a1 - self.a2) ** 2) + ((self.b1 - self.b2) ** 2)) ** 0, 5
        sqr_square = side**2
        return sqr_square

"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""
if __name__ == "__main__":
    circle = Circle(1,2,3)
    triangle = Triangle(1,2,4,5,8,7)
    square = Square(1,5,3,6)

    figures = [circle, triangle, square]

print(figures)

