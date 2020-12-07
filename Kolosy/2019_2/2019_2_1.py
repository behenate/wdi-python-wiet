"""
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.

"""
import random
random.seed(0)
t1 = [random.randint(0,9) for _ in range(20)]
random.seed(1)
t2 = [random.randint(0,9) for _ in range(20)]
print(t1, t2)

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True
def prime_multi(n):
    for i in range(2, int(n**1/2)+1):
        for j in range(2, int(n**1/2)+1):
            if i*j == n:
                if is_prime(i) and is_prime(j):
                    return True
    return False

def da_sie(t1,t2):
    N = len(t1)
    for x in range(1, N+1):
        for y in range(N-x+1):
            suma1 = 0
            for i in range(y, x+y):
                suma1 += t1[i]
            for y1 in range(N - x + 1):
                suma2 = 0
                for i1 in range(y1, y1+x):
                    suma2 += t2[i1]
                    if suma1 == suma2:
                        if prime_multi(suma1):
                            return True

    return False

print(da_sie(t1,t2))