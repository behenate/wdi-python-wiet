"""

Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero

"""


def sprawdz(tab):
    N = len(tab)
    for start in range(N):
        prev_pos = [[-10 for _ in range(2)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if prev_pos[0] == [-10, -10]:
                    prev_pos[0] = [y, start]
                    break
                can_place = True
                for k in range(0, y):
                    if not (abs(prev_pos[k][0] - x) >= 3 or abs(prev_pos[k][1] - y) >= 3):
                        can_place = False
                        break
                if can_place:
                    prev_pos[y] = [x, y]
                    break
        # print(prev_pos)
        ret = True
        for elem in prev_pos:
            if elem[0] == -10 or elem[1] == -10:
                ret = False
        if ret:
            print( prev_pos)



tab = [
    [ 5,  5,  5,  5,  5,  5,  5,],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [-5, -5, -5, -5, -5, -5, -5]
]

print(sprawdz(tab))
