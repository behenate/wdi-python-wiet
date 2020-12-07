"""

Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
pozostać nie zmieniane.


"""

import random


def compare(n1, n2):
    l1 = l2 = 0
    _n1 = n1
    _n2 = n2
    while _n1 > 0:
        l1 += _n1 % 2
        _n1 /= 2
    while _n2 > 0:
        l2 += _n2 % 2
        _n2 /= 2
    if l1 == l2:
        return True
    return False


w1 = 100
w2 = 4
T1 = [[random.randint(0, 999) for _ in range(w1)] for _ in range(w1)]
T2 = [[random.randint(0, 999) for _ in range(w2)] for _ in range(w2)]

is_more = False
for i in range(w1-w2+1):
    for j in range(w1-w2+1):
        score = 0
        for k in range(w2):
            for l in range(w2):
                if compare(T1[i+k][j+l], T2[k][l]):
                    score += 1
        score /= w2**2
        if score > 0.33:
            is_more = True
            break
    if is_more:
        break

print("Jest? {}".format(is_more))