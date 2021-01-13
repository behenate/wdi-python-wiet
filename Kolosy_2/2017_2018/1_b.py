"""
Zadanie 1.
Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool.

"""
from random import randint, seed

seed(10)

N = 8
T = [[randint(1, 10) for _ in range(N)] for _ in range(N)]


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while (i - 1) ** 2 <= n:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    return True


vectors = ((1, -2), (2, -1), (2, 1), (1, 2))


def can_place(T):
    for y in range(N):
        for x in range(N):
            n1 = T[y][x]
            for vector in vectors:
                if 0 <= y + vector[0] < N and 0 <= x + vector[1] < N:
                    n2 = T[y + vector[0]][x + vector[1]]
                    if is_prime(n1 + n2):
                        print(y, x, y + vector[0], x + vector[1], "  ", n1 + n2)
    return False


print(can_place(T))
for line in T:
    print(line)
