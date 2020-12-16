"""
Zadanie 24. Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
2 niepustych podzbiorów tego zbioru.
"""
from random import randint, seed
from copy import deepcopy

seed(0)


def center_of_mass(T, cnt):
    x = y = 0
    for elem in T:
        x += elem[0]
        y += elem[1]
    return x / cnt, y / cnt


def dist(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))**(1/2)


def center_subsets(T, pos=-1, t1_l=0, t2_l=0, take=0):
    if pos == len(T):
        return False
    if take == 0:
        Tc1[pos] = T[pos]
    elif take == 1:
        Tc2[pos] = T[pos]

    if t1_l >= 1 and t2_l >= 1:
        print(Tc1, Tc2)
        c1 = center_of_mass(Tc1, t1_l)
        c2 = center_of_mass(Tc2, t2_l)
        d = dist(c1, c2)
        global min_dist
        if d < min_dist:
            min_dist = d

    ret=center_subsets(T, pos+1, t1_l+1, t2_l, 0) or \
        center_subsets(T, pos+1, t1_l, t2_l+1, 1) or \
        center_subsets(T, pos+1, t1_l, t2_l, 2)
    if ret:
        return ret
    if take == 0:
        Tc1[pos] = (0, 0)
    elif take == 1:
        Tc2[pos] = (0, 0)


# T = [[randint(0, 20) for _ in range(2)] for _ in range(5)]
T = [(0,0),(1,2),(2,1),(100000000,1000000000)]
Tc1 = [(0, 0) for _ in range(len(T))]
Tc2 = [(0, 0) for _ in range(len(T))]
min_dist = 999
for line in T:
    print(line)
center_subsets(T)
print(min_dist)