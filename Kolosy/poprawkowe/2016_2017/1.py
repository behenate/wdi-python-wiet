"""
Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
która zwróci długość tego ciągu.
"""
from random import randint, seed
from time import time
start = time()
def czy_pierwsza(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**(1/2))+1, 2):
        if n % i == 0:
            return False
    return True

N = 1000
seed(3)
t = [[randint(0,1000) for _ in range(N)] for _ in range(N)]

t1 = [[0 for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        t1[y][x] = t[y][x] if czy_pierwsza(t[y][x]) else -1

y=0
x=0
max_cnt = 1
while y < N:
    r_old = None
    cnt = 1
    x = 0
    while x < N-1:
        a = t1[y][x]
        b = t1[y][x+1]
        r = b-a
        if a == -1:
            x += 1
            r_old = None
            cnt = 1
            continue
        if r_old is None:
            r_old = r
        elif r == r_old and b != -1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
            x += 1
        else:
            cnt = 1
            r_old = None
            x += 1
    y += 1
    # print(max_cnt)
print("----")
x = y = 0
while x < N:
    r_old = None
    cnt = 1

    y = 0
    while y < N-1:
        a = t1[y][x]
        b = t1[y+1][x]
        r = b-a
        if a == -1:
            y += 1
            r_old = None
            cnt = 1
            continue
        if r_old is None:
            r_old = r
        elif r == r_old and b != -1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
            y += 1
        else:
            cnt = 0
            r_old = None
            y += 1
    x += 1
print(max_cnt)

print(time()-start)

