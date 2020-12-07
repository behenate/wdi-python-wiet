"""

Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.

"""


def ruch(i, j, licznik):  # wiersz, kolumna, licznik
    licznik += 1
    tab[i][j] = licznik
    if licznik == n * n:
        return True
    for wektor in weks:
        if 0 <= i + wektor[0] < n and 0 <= j + wektor[1] < n:
            if tab[i + wektor[0]][j + wektor[1]] == 0:
                if ruch(i + wektor[0], j + wektor[1], licznik):
                    return True
    tab[i][j] = 0
    return False


n = 8
weks = ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1))
tab = [[0 for _ in range(n)] for _ in range(n)]

ruch(2, 4, 0)

for i in range(n):
    print(tab[i])
