from random import randint, seed
import time
seed(0)
start = time.time()
def det_2_2(tab, x, rows):
    return (tab[rows[0]][x] * tab[rows[1]][x+1]) - (tab[rows[0]][x+1] * tab[rows[1]][x])


def rekur_det(matrix, x, row_tab):
    sum = 0
    s_x = 0
    # print(row_tab)
    for i,elem in enumerate(row_tab):
        next_rows = [0]*(len(row_tab)-1)

        cnt = 0
        for e in row_tab:
            if e != elem:
                next_rows[cnt] = e
                cnt += 1

        if len(next_rows) == 2:
            sum += (-1)**(i) * matrix[elem][x] * det_2_2(matrix, x+1, next_rows)
        else:
            smol_det = rekur_det(matrix, x+1, next_rows)
            add = (-1)**(i) * matrix[elem][x] * smol_det
            sum += add
    return sum


matrix = [
    [6, 6, 6, 7],
    [7, 5, 8, 4],
    [0, 1, 2, 5],
    [11, 5, 6, 7]
]
matrix = [[randint(1,20) for _ in range(10)] for _ in range(10)]

print(rekur_det(matrix, 0, [i for i in range(len(matrix))]))
print(time.time()-start)