"""

Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. N z zakresu 4...20.

"""
from random import random, getrandbits, seed


def ma_droge(x, y, t):
    if 0 <= x < N and 0 <= y < N:
        if y == N - 1:
            return True
        if t[y][x]:
            return False
        return ma_droge(x+1, y+2, t) or ma_droge(x-1, y+2, t) or ma_droge(x+2, y+1, t) or ma_droge(x-2, y+1, t)
    else:
        return False


seed(0)
N = 10
tab = [[bool(getrandbits(1)) for _ in range(N)] for _ in range(N)]
for line in tab:
    print(line)

for i in range(N):
    print(i)
    if ma_droge(i, 0, tab):
        print(i)
        print("Znalazło!")
        break
