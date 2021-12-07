"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости (скорость
 +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задния ход (изменение
 знака скорости)
"""

class car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def change_speed(self):
        self.speed +=5
        print(self.speed)

    def min_speed(self):
        self.speed -=5
        print(self.speed)

    def now_speed(self):
        print(self.speed)








