"""
Zadanie 2.
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
warto±¢ typu bool.
"""

from random import randint, seed



N = 4
t = [randint(0, 9) for i in range(N)]
print(t)


def subsets(p1=0, p2=0, l1=0, l2=0, i=0, set_1=None, set_2=None):
    if set_1 is None or set_2 is None:
        set_1 = []
        set_2 = []
    if l1 > 0 and l1 == l2 and p1 == p2:
        print(set_1, set_2)
        return True
    if i >= len(t):
        return False
    ret = False
    ret = subsets(p1 + t[i], p2, l1+1, l2, i+1, set_1+[t[i]], set_2)or\
    subsets(p1, p2 + t[i], l1, l2+1, i+1, set_1, set_2+[t[i]])or\
    subsets(p1, p2, l1, l2, i+1, set_1, set_2)
    return ret
print(subsets())