import random
t = [
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
]
N = 9
t = [[random.randint(2, 102) for _ in range(N)]for _ in range(N)]


def ustaw_wiersz(tab, row, prev, s, N):
    if row == N:
        if s == 0:
            return True
    else:
        for a in range(N):
            if abs(prev - a) > 1:
                jest = ustaw_wiersz(tab, row+1, prev=a, s=s+tab[row][a], N=N)
                if jest:
                    return jest
    return False
N = len(t)
print(ustaw_wiersz(t, 0, -2, 0, N))