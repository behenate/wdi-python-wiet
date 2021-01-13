'''
Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero.
'''

from random import randint, seed
seed(2)
N = 4
T = [[randint(-5,5) for _ in range(N)] for _ in range(N)]
for line in T:
    print(line)


def find_place():
    def recur_place(n, pos, prev_pos, s=0, pozycje=[]):
        if abs(prev_pos[1] - pos[1]) < 2:
            return False
        if pos[0] == n-1:
            pozycje += [pos]
            s += T[pos[0]][pos[1]]
            if s == 0:
                print(pozycje)
                return True
            return False
        for i in range(n):
            if recur_place(n, (pos[0]+1, i), pos, s+T[pos[0]][pos[1]], pozycje+[pos]):
                return True
        return False

    for i in range(N):
        print(recur_place(N, (0, i), (-100,-100), 0, []))
find_place()