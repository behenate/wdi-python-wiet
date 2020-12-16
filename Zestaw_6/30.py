"""
Zadanie 30. Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
wartość typu bool.
"""

tab = [(-20, -20), (20, 20), (5, 5), (-5, -5), (15, 20), (33, -2), (12, -23)]
Tp = [(0,0) for _ in range(len(tab))]

def center_of_mass(T, cnt):
    x = y = 0
    for elem in T:
        x += elem[0]
        y += elem[1]
    return x/cnt, y/cnt


def dist(p):
    return ((p[0]**2) + (p[1]**2))**(1/2)


def find_dist_subset(T, r, k, pos=-1, tp_l=0, take=False):
    if pos != -1 and take:
        Tp[pos] = T[pos]
    if tp_l > k:
        print(Tp)
        c_o_m = center_of_mass(Tp, tp_l)
        if dist(c_o_m) < r:
            return True
    if pos == len(T)-1:
        Tp[pos] = (0, 0)
        return False
    ret = find_dist_subset(T, r, k, pos+1, tp_l+1, True) or\
        find_dist_subset(T, r, k, pos+1, tp_l, False)
    if ret:
        return True
    Tp[pos] = (0, 0)
    return False


print(find_dist_subset(tab, 3, 3))
