"""
Zadanie 20. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
"""
import time
import random
start = time.time()
random.seed(0)
tab = [[random.randint(0,9) for _ in range(20)] for _ in range(20)]
print(tab)
n = len(tab)
y = 0
x = 2
sum_1 = 0
m = 0
m_index = (0,0,0,0)
for y in range(n):
    for x in range(n):
        sum_1 = 0
        for r in range(n):
            if r != y:
                sum_1 += tab[r][x]
            if r != x:
                sum_1 += tab[y][r]
        for y_1 in range(n):
            for x_1 in range(x, n):
                sum_2 = 0
                if x_1 != x and y_1 != y:
                    for r in range(n):
                        if r != y_1 and r != y:
                            sum_2 += tab[r][x_1]
                        if r != x_1 and r != x:
                            sum_2 += tab[y_1][r]

                if (sum_1+sum_2) > m:
                    print(sum_1, sum_2)
                    m = (sum_1 + sum_2)
                    m_index = (x, y, x_1, y_1)
print(m, m_index)

print(time.time()-start)