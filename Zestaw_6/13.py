"""
Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""
from time import time
start = time()
def decay(n, ret="", last=1):
    if n == 0:
        print(ret)
    if n < 0:
        return
    for i in range(last, n+1):
        decay(n-i, "{}+{}".format(ret, i), i)


num = 4
decay(num)
print(time()-start)

