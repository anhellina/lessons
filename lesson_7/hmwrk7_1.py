import math

def ch(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (abs(x1 - x2) == 2 or abs(y1 - y2) == 2) and (abs(x1 - x2) == 1 or abs(y1 - y2) == 1):
        return True
x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))

x2 = int(input("enter x2: "))
y2= int(input("enter y2: "))

if ch(x1, y1, x2, y2):
    print('yes')
else:
    print('no')