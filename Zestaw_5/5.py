"""

Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
[(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze
 istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
punktów.

"""
import random
import time
start = time.time()
# t = [(6, 2), (2, 6), (6, 6), (2, 2)]
random.seed(0)
t = [(random.randint(0, 10000),random.randint(0, 10000)) for _ in range(5000)]

dict = {}
for elem in t:
    dict[elem] = 0

def find_candidates(sp, diff):
    tc1 = sp[0], sp[1] - diff[1]
    tc2 = sp[0] - diff[0], sp[1]
    return tc1 in dict and tc2 in dict, tc1, tc2


def collision(p1, p2, p3, p4, tab):
    for elem in tab:
        if min(p1[0], p4[0]) < elem[0] < max(p1[0], p4[0]) and max(p1[1], p4[1]) < elem[1] < min(p1[1], p4[1]):
            return True
    return False


def find_sqr(tab):
    N = len(tab)
    for i in range(N-1):
        p1 = tab[i]
        for j in range(i+1, N):
            p4 = tab[j]
            diff = (p1[0] - p4[0]), (p1[1] - p4[1])
            if abs(diff[0]) == abs(diff[1]):
                found, p2, p3 = find_candidates(p1, diff)
                if found and not collision(p1, p2, p3, p4, tab):
                    print(p1, p4, p2, p3)
                    return True

    return False


print(find_sqr(tab=t))
print(time.time()-start)