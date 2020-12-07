"""
Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt
przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.

"""
from random import randint, seed
import math
seed(1)
T = [[10, 5, 8, 9, 9, 3, 4, 10],
       [5, 4, 1, 4, 3, 10, 9, 7],
       [2, 9, 4, 1, 3, 9, 8, 7],
       [8, 8, 1, 4, 6, 6, 6, 3],
       [10, 1, 10, 6, 8, 3, 3, 10],
       [10, 6, 1, 10, 1, 5, 10, 4],
       [1, 10, 6, 2, 6, 7, 3, 10],
       [10, 7, 5, 5, 4, 2, 5, 10]]
for line in T:
    print(line)

def ruch(y, x, cost):
    if x < 0 or x > 7:
        return math.inf
    cost += T[y][x]
    if y == 7:
        return cost

    s1 = ruch(y+1, x, cost)
    s2 = ruch(y+1, x-1, cost)
    s3 = ruch(y+1, x+1, cost)
    return min(s1, s2, s3)

print(ruch(0, 0, 0))
smol = math.inf

r = ruch(0, 0, 0)
print(1, r)
