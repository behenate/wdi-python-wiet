from random import randint, seed
seed(10)

N = 4
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]
# T=[[0,0,0,0,0,0,0,100],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0]
# ]
def calc_sum(T, pos1, pos2):
    sum = 0
    for i in range(N):
        if i == pos1[0] or T[i][pos1[1]] == pos2:
            continue
        sum += T[i][pos1[1]]

    for i in range(N):
        if i == pos1[1] or T[i][pos1[1]] == pos2:
            continue
        sum += T[pos1[0]][i]

    for i in range(N):
        if i == pos2[0] or i == pos1[0] or pos1[0] == pos2[0]:
            continue
        sum += T[i][pos2[1]]

    for i in range(N):
        if i == pos2[1] or i == pos1[1] or pos1[1] == pos2[1]:
            continue
        sum += T[pos2[0]][i]
    return sum


for line in T:
    print(line)
def can_move(T, tower1, tower2):
    maximum = 0
    start_sum = calc_sum(T, tower1, tower2)
    wspolrzedne = None
    for i in range(N):
        if i == tower1[0]:
            continue
        temp_sum = calc_sum(T, [i, tower1[1]], tower2)
        print(temp_sum, start_sum, [i, tower1[1]])
        if temp_sum > maximum:
            maximum = temp_sum
            wspolrzedne = ([i, tower1[1]], tower2)
        # if temp_sum > start_sum:
        #     return True

    for i in range(N):
        if i == tower1[0]:
            continue
        temp_sum = calc_sum(T, [tower1[0], i], tower2)
        if temp_sum > maximum:
            maximum = temp_sum
            wspolrzedne = ([i, tower1[1]], tower2)
        # if temp_sum > start_sum:
        #     return True

    for i in range(N):
        if i == tower2[0]:
            continue
        temp_sum = calc_sum(T, [i, tower2[1]], tower1)
        if temp_sum > maximum:
            maximum = temp_sum
            wspolrzedne = ([i, tower2[1]], tower1)
        # if temp_sum > start_sum:
        #     return True

    for i in range(N):
        if i == tower2[1]:
            continue
        temp_sum = calc_sum(T, [tower2[0], i], tower1)
        maximum = max(temp_sum, maximum)
        if temp_sum > maximum:
            maximum = temp_sum
            wspolrzedne = ([i, tower2[1]], tower1)
        # if temp_sum > start_sum:
        #     return True
    return maximum, wspolrzedne
print(can_move(T, (0,0), (N-1,N-1)))