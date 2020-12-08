"""
Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool
"""
def tab_sum(T, num):
    def find_sum(p_c, sum = 0, index=0):
        if sum == num:
            print(sum)
            return True
        if sum > num or index == n:
            return False
        found = False
        for i in range(n):
            if p_c[i]:
                continue
            pc = p_c[:]
            pc[i] = True
            found = found or find_sum(pc, sum + T[index][i], index+1)
        found = found or find_sum(p_c, sum, index+1)
        return found

    n = len(T)
    prohibited_cols = [False for _ in range(n)]
    return find_sum(prohibited_cols)

T = [
    [1,3],
    [1,7]
]
print(tab_sum(T, 10))