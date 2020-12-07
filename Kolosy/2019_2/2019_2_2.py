"""

Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy był wielokrotnością
(co najmniej dwukrotnością) kwadratu dowolnej liczby naturalne większej od 1.

"""
import random
from math import ceil

def w_k(num):
    b = int(num**(1/2)+1)
    for n in range(2, b):
        n_1 = n**2
        for i in range(2, int(num/2)):
            if n_1 * i == num:
                return True
    return False

random.seed(1)
N = 7
t = [[random.randint(2, 102) for _ in range(N)]for _ in range(N)]
t_t =[[False for _ in range(N)]for _ in range(N)]

for y in range(N):
    for x in range(N):
        t_t[y][x] = w_k(t[y][x])

for w in range(N):
    for k1 in range(N):
        for k2 in range(k1+1, N):
            jes = True
            for y in range(N):
                for x in range(N):
                    if x!= k1 and x != k2 and y != w:
                        jes = jes and(t_t[y][x])
            if jes:
                print(w, k1, k2)


