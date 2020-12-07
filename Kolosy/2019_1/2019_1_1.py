"""
    Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
    sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
    co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
"""
from random import randint


def potega(n, a):
    while n > 1:
        if n % a != 0:
            return False
        n //= a
    return True


N = 1000
t1 = [randint(1,10) for i in range(N)]
t2 = [randint(1,10) for i in range(N)]
a=6
# t1 = [1,0,0,1,1,0,1,1,1,0,0,0,1]
# t2 = [0,0,0,0,0,0,1,1,1,0,0,0,1]
found = False
for i in range (1, min(len(t1)+1, 25)):
    for j in range((len(t1) - i) +1):
        w1 = t1[j:j+i]
        s1=0
        for elem in w1:
            s1 += elem

        w2_len = 24 - i
        for k in range((len(t2)-w2_len)+1):
            w2 = t2[k:k+w2_len]
            s2 = 0
            for elem in w2:
                s2 += elem
            s = int((s1+s2)**(0.5))

            if potega(s1+s2, a):
                print(s1, s2, w1, w2)
                found = True
                break
        if found:
            break
    if found:
        break

