"""
Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
"""
n = int(input("n:"))
m = int(input("m:"))
result = 0
for x in range(n, m + 1):
    result += x ** 3 
    
print(result)

