"""
Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
"""


def licz_n_ki(T, target, n, start=0):
    if target == 1 and n == 0:
        return 1
    if n == 0:
        return 0
    cnt = 0
    for i in range(start, len(T)):
        if target % T[i] == 0:
            cnt += licz_n_ki(T, target // T[i], n - 1, i + 1)
    return cnt


tab = [2, 2, 2, 2, 2]
print(licz_n_ki(tab, 16, 4))
