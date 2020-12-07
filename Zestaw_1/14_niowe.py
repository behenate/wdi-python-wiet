from math import *
import time
# Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina
# x0 = 0
# f(x) = f(x) + f'(0)x
# Zakładam, że wiadomo że cos(x)=1 cos'(x)=0 cos''(x) = -1  cos'''(x) = 0 i cos''''(x) = cos(x) itd.

def silnia(y):
    i=y
    # 5 4 3 2 1
    while y<1:
        y-=1
        i *= y
    return i


wynik = 1
prev = 0
accuracy = 0.0000001

i = 1
x = pi/6

while abs(prev-wynik) > accuracy:
    prev = wynik
    if i % 2 == 0:
        wynik += (1/silnia(i*2)) * pow(x, i*2)
    else:
        wynik -= (1/silnia(i*2)) * pow(x, i*2)
    i += 1

print(wynik)