"""
2. Proszę napisać program, który wypełnia tablicę int tab[MAX] liczbami pseudolosowymi
z zakresu [1 .. 1000], a następnie wyznacza i wypisuje sumę 10 największych elementów
z tablicy.
Uwagi:
- tablica tab zajmuje ponad połowę dostępnej pamięci na dane i nie może ulec zmianie

"""
from random import randint
from copy import copy
from time import time
start = time()
N = 1000000
tab = [randint(1,1000) for _ in range(N)]
N = len(tab)
t_b = [0 for _ in range(10)]

for i in range(N):
    for j in range(10):
        if tab[i] > t_b[j]:
            temp = copy(t_b)
            for k in range(j+1, 10):
                t_b[k] = temp[k-1]
            t_b[j] = tab[i]
            break

print(time()-start)