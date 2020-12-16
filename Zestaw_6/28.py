"""
Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → f alse, podział nie istnieje.
"""


def count_ones(tab):
    cnt_tab = [0]*len(tab)
    for y in range(len(tab)):
        for elem in tab[y]:
            num = elem
            cnt = 0
            while num > 0:
                cnt += num % 2
                num //= 2
            cnt_tab[y] += cnt
    return cnt_tab


def find_subsets(index, pos, value):
    Tp[pos[0]][pos[1]] = value
    if index == len(T):

        t = count_ones(Tp)
        if t[0] == t[1] and t[1] == t[2]:
            print(Tp)
            return True
        Tp[pos[0]][pos[1]] = 0
        return False
    res = find_subsets(index+1, [0, index], T[index]) or \
        find_subsets(index + 1, [1, index], T[index]) or \
        find_subsets(index + 1, [2, index], T[index])
    if res:
        return True
    Tp[pos[0]][pos[1]] = 0
    return res

T = [2, 3, 5, 7, 15]
Tp = [[0 for _ in range(len(T))] for _ in range(3)]

print(find_subsets(0, [0, 0], [2, 3, 5, 7, 15]))