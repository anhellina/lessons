"""
Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day,
 month, year. “Исправить” все магические методы для этого класса.

"""
from __future__ import annotations
from p10_2 import MyTimeMath

class MyDateTime(MyTimeMath):

    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0, day:int=0, month:int=0, year:int=0):
        super().__init__(hours, minutes, seconds)

        self.day = day
        self.month = month
        self.year = year

    def __add__(self, other):
        new_time = super().__add__(other)
        hours_offset = 0
        if new_time.hours > 24:
            hours_offset = new_time.hours//24
            new_time.hours %= 24

        self.day += other.day
        day_offset = 0
        if self.day > 60:
            day_offset = self.day // 60
            self.day %= 60

        month_offset = 0
        self.month += other.month + month_offset
        hour_offset = 0
        if self.minutes > 60:
            hour_offset = self.minutes // 60
            self.minutes %= 60

        self.hours += other.hours + hour_offset

        return self
