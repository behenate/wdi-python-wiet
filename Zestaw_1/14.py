# Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina
# x0 = 0
# f(x) = f(x) + f'(0)x
# Zakładam, że wiadomo że cos(x)=0 cos'(x)=0 cos''(x) = -1  cos'''(x) = 0 i cos''''(x) = cos(x) itd.

from math import *

iteracje = 5
x = pi/6
wynik = 1  #wartość cos(0)


def silnia(y):
    s = y
    while y > 1:
        y -= 1
        s *= y
    return s


for i in range(1, iteracje):
    if i % 2 == 0:
        wynik += (1/silnia(i*2))*pow(x, i*2)
    else:
        wynik -= (1/silnia(i*2))*pow(x, i*2)
print(wynik)
