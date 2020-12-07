"""
Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą.


"""
from generator import generuj_spirale, printuj_spirale

def wystepuje(tab):
    truth_tab = [[False for _ in range(len(tab))] for _ in range(len(tab[1]))]

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
                    truth_tab[i][j] = True
                num //= 10
    final = False
    for line in truth_tab:
        res = True
        for elem in line:
            if not elem:
                res = False
        final = final or res
    return final


tab = [[22,32,22], [11,11,11], [5,4,2]]
print(wystepuje(tab))
printuj_spirale(tab)