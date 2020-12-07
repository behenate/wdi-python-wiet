"""
Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
"""


def licz_n_ki(T, target, n, start=0, comb=[]):
    if len(comb) == 0:
        comb = [0] * len(T)
    if target == 1 and n == 0:
        print("Found! Used numbers: ", end="")
        for elem in comb:
            if elem != 0:
                print(elem, end=", ")
        print()
        return 1
    if n == 0:
        return 0

    cnt = 0
    for i in range(start, len(T)):
        if target % T[i] == 0:
            a = comb[:]
            a.append(T[i])
            cnt += licz_n_ki(T, target // T[i], n - 1, i + 1, a)
    return cnt


tab = [4, 1, 5, 7, 9, 4, 5, 9, 6, 5, 3, 2, 7, 6, 1, 1, 7, 9, 9, 1]
print(licz_n_ki(tab, 24, 3))
