"""
Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy
ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.
"""
from one import *

tab = [(1, 2), (1, 4), (1, 8), (1, 16), (1, 3), (1, 2), (1, 4), (1, 8), (1, 16), (1, 32), (1, 1), (2, 1), (3, 1),
       (4, 1)]
tab = [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]
n = len(tab)


def count_geo(tab):
    i = 0
    max_len = 0
    ln = 1
    q = (0, 0)
    while i < n - 1:
        if q == (0, 0):
            q = div(tab[i + 1], tab[i])
            ln = 1
        if multi(tab[i], q) == tab[i + 1]:
            ln += 1
            max_len = max(max_len, ln)
        else:
            q = (0, 0)
            ln = 0
            i -= 1
        i += 1
    return max_len

def how_many_2s(n):
    total = 0
    for i in range(3, n+1):
        total += n - i + 1
    return total


def count_art(tab):
    i = 0
    max_len = 0
    ln = 0
    total = 0
    r = None
    while i < n - 1:
        if r is None:
            r = sub(tab[i + 1], tab[i])
            ln = 1
        if add(tab[i], r) == tab[i + 1]:
            ln += 1
            max_len = max(max_len, ln)
        else:
            r = None
            if ln > 4:
                print(how_many_2s(ln), ln)
                total += how_many_2s(ln)
            ln = 0
            i -= 1
        i += 1
    if ln > 4:
        total += how_many_2s(ln)
    return total



print(count_art(tab))
