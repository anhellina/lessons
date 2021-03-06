"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3. На стержень 1 надета пирамидка
 из n дисков различного диаметра в порядке возрастания диаметра. Диски можно перекладывать с одного стержня на другой
 строго по одному, при этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю пирамидку со
 стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний,
необходимую для решения головоломки
"""
n = 5                                           # Количество дисков

def play(n, sourse, receiver, storage):
    """
    Функция перемещения n дисков в головоломке Ханойская башня.
    Аргументы функции:
    Первый аргумент n - integer (целое число), количество дисков в пирамиде.
    sourse, receiver, storage - любого типа.
    Второй аргумент - sourse, стержень с которого перекладываем диски.
    Третий аргумент - receiver, стержень на который перекладываем диски.
    Четвёртый аргумент - storage, стержень на который перекладываем n-1 дисков
    для временного хранения в процессе общей работы.
    """
    if n <= 0: return
    play(n-1, sourse, storage, receiver)
    print("Диск ", n, " : ", sourse, " --> ", receiver)
    play(n-1, storage, receiver, sourse)

play (n, 'a', 'b', 'c')