"""
Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров. В первый день спортсмен пробежал
Y километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. Определите номер дня в который
спортсмен достигнет своей цели. Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит
номер найденного дня.
"""
y = int(input("enter y:"))
x = int(input("enter x:"))

day = 0
while y<x :
    y = y + y*1,1
    day +=1
print(day)

