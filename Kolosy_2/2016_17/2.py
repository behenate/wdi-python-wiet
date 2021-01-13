"""
Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
funkcja powinna zwrócić położenie wież.
"""
from random import randint, seed
seed(69)
N = 50
T = [[randint(1, 10) for _ in range(N)] for _ in range(N)]

for line in T:
    print(line)
sum_cols = [0]*N
sum_rows = [0]*N

for y in range(N):
    for x in range(N):
        sum_rows[y] += T[y][x]

for x in range(N):
    for y in range(N):
        sum_cols[x] += T[y][x]


def calc_sum(t1, t2):
    s = sum_rows[t1[0]] + sum_cols[t1[1]] - 2*(T[t1[0]][t1[1]])

    if t1[0] != t2[0]:
        s += sum_cols[t2[1]]
        if t1[1] != t2[1]:
            s -= T[t2[0]][t1[1]]
        s -= T[t2[0]][t2[1]]

    if t1[1] != t2[1]:
        s += sum_rows[t2[0]]
        if t1[0] != t2[0]:
            s -= T[t1[0]][t2[1]]
        s -= T[t2[0]][t2[1]]
    return s

print(calc_sum((0,1), (1,1)))
max_sum = 0
mx,my,mx1,my1 = 0,0,0,0
for y in range(N):
    for x in range(N):
        for y1 in range(N):
            for x1 in range(N):
                if calc_sum((y, x), (y1, x1)) > max_sum and (x != x1 and y != y1):
                    max_sum = calc_sum((y, x), (y1, x1))
                    my,mx,my1,mx1  = y,x,y1,x1

print(max_sum)
print(my,mx,my1, mx1)