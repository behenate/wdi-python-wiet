import time
start = time.time()
def generuj_spirale(tab):
    n = len(tab)
    k = 1
    a = 0
    b = n-1
    while a<=b:
        for i in range(a, b+1):
            tab[a][i] = k
            k += 1

        for i in range(a+1, b):
            tab[i][b] = k
            k += 1

        for i in range(b, a, -1):
            tab[b][i] = k
            k += 1

        for i in range(b, a, -1):
            tab[i][a] = k
            k += 1
        a += 1
        b -= 1

generuj_spirale([[0 for _ in range(10000)] for _ in range(10000)])
print(time.time()-start)