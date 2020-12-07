"""
Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
o 2 niewiadomych.
"""
from one import *
"""
ax + by = c
y = c/b - ax/b
"""
def uklad(w1, w2):
    a, b, c = w1
    d, e, f = w2
    y = div(przec(a), b)
    c = div(c, b)
    wolny = div(sub(f, multi(c, e)), d)
    wyn_x = add(multi(y, e), d)
    res_x = div(wolny, wyn_x)

    res_y = div(sub(f, multi(res_x, d)), e)
    print("x: {}, y: {}".format(res_x, res_y))
    res_x, res_y
w1 = ((2,1), (1,1), (3,1))
w2 = ((1,1), (1,1), (1,1))
print(uklad(w1,w2))