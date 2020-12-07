
import random
import time
N = 25
# tab = [[randint(1,100) for i in range(N)] for j in range(N)]
# for i in range(N):
# print(tab[i])
random.seed(0)
print(random.randint(0,9))
start = time.time()

tab = [[random.randint(0,9) for _ in range(20)] for _ in range(20)]

N = len(tab)

sumkol = [0] * N
sumwier = [0] * N

for i in range(N):
    for j in range(N):
        sumwier[i] += tab[i][j]
        sumkol[i] += tab[j][i]

# i, j - połozenie 1 wiezy
# a, b = położenie 2 wieży
maxsum = 0
_a = 0
_b = 0
_i = 0
_j = 0

for i in range(N):
    for j in range(N):
        for a in range(i, N):
            for b in range(N):
                if (a != i or b != j):
                    suma = sumwier[i] + sumkol[j] + sumwier[a] + sumkol[b]
                    if (i == a):
                        suma = suma - sumwier[i]
                    if (j == b):
                        suma = suma - sumkol[j]
                    suma = suma - 2 * tab[i][j] - 2 * tab[a][b]
                    if (i != a and j != b):
                        suma = suma - tab[i][b] - tab[a][j]
                    if (suma > maxsum):
                        _a, _b, _i, _j, maxsum = a, b, i, j, suma

print("(" + str(_i) + "," + str(_j) + "), (" + str(_a) + "," + str(_b) + ") suma:" + str(maxsum))
print(time.time()-start)