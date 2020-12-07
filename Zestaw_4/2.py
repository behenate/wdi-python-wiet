"""
Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr
"""
from generator import generuj_spirale, printuj_spirale

def wystepuje(tab):
    truth_tab = [[True for _ in range(len(tab))] for _ in range(len(tab[1]))]

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            i_c = 0
            num = tab[i][j]
            while num > 0:
                num //= 10
                i_c += 1
            num = tab[i][j]
            print(tab[i][j])
            for _ in range(i_c):
                if (num % 10) % 2 == 0:
                    truth_tab[i][j] = False
                num //= 10
    final = True
    for line in truth_tab:
        res = False
        for elem in line:
            res = res or elem
        if not res:
            final = False
            break
    return final


tab = generuj_spirale(3)
print(wystepuje(tab))
printuj_spirale(tab)