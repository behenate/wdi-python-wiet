"""
Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
posiadał nieparzystą liczbę jedynek.
"""
n = 7
t = [
    [4, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3],
    [3, 3, 4, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3]
]

for rw in range(n):
    for rk1 in range(n-1):
        for rk2 in range(rk1+1, n):
            is_ones = True
            for y in range(n):
                if y != rw:
                    for x in range(n):
                        if x != rk1 and x != rk2:
                            num = t[y][x]
                            while num > 0:
                                if num % 2 == 0:
                                    is_ones = False
                                    break
                                num//=2
                    if not is_ones: break
            print(is_ones)
            if not is_ones: break

