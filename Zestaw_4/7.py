"""

Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco.

"""

import time
start = time.time()
# MAX=n = 200
# T1 = [[i+(j*MAX) for i in range(MAX)] for j in range(MAX)]
# T2 = [0 for _ in range(MAX*MAX)]
T1 = [
    [3, 4, 5],
    [1, 2, 2],
    [1, 10, 20]
]
n = len(T1)
T2 = [0]*(n*n)
for i in range(n):
    for j in range(n):
        for k in range((n**2)-1, -1, -1):
            if T1[i][j] > T2[k]:
                t1 = T2[1:k+1]
                t2 = T2[k+1:]
                T2 = t1 + [T1[i][j]] + t2
                break
print(T2)
print(time.time()-start)