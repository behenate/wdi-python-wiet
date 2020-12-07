from random import randint
import time
start = time.time()

def wyznacznik(j,tabwierszy): #kolumna,tab wierszy
    if(j+1==len(tab)):
        for i in range(len(tab)):
            if(tabwierszy[i]):
                return tab[i][j]
    suma = 0
    d=0
    for i in range(len(tab)):
        if(tabwierszy[i]):
            tabwierszy_copy = tabwierszy[:]
            tabwierszy_copy[i] = 0
            suma=suma+((-1)**(d))*(tab[i][j])*(wyznacznik(j+1,tabwierszy_copy))
            d+=1
    return suma


tab =  [
    [6, 6, 6, 7],
    [7, 5, 8, 4],
    [0, 1, 2, 5],
    [11, 5, 6, 7]
]

tab = [[randint(1,20) for _ in range(10)] for _ in range(10)]


tabwierszy = [1]*len(tab)

print(wyznacznik(0,tabwierszy))
print(time.time()-start)

