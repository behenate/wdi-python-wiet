# Dane są ciągi: An+1 =√An ∗ Bn oraz Bn+1 = (An + Bn)/2.0.
# Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.

from math import *
import time
a = 24
b = 6
n = 1
while True:
    n += 1
    a_n1 = sqrt(a * b)
    b_n1 = (a + b)/2
    a = a_n1
    b = b_n1
    if a == b:
        print(a)
        break
