"""
Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą równanie kwadratowe o współczynnikach
zespolonych.
"""

from six_1 import *

"""Zakładam, że równanie jest w postaci ax^2 + bx + c = 0"""


def equation(w1):
    a, b, c = w1

    delta = sub(pow(b, 2), multi(multi(a, c), (4, 0)))
    print(delta)


w1 = (0, 1), (0, 1), (0, 1)
print(equation(w1))
