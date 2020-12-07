"""
Zadanie 15. Problem 8 Hetmanów (treść oczywista)
"""
import time
start = time.time()

def can_place(pos, queens):
    for queen in queens:
        if queen[0] == -1:
            break
        y = queen[0]
        x = queen[1]
        diff = queen[0] - queen[1]
        sum = queen[0] + queen[1]
        if pos[0] == y or pos[1] == x or pos[0] - pos[1] == diff or pos[0] + pos[1] == sum:
            return False
    return True


def place_queen(T, pos, queens, N, i=0):
    ret = False
    if pos[0] == N:
        print(queens)
        return True
    if can_place(pos, queens):
        queens[i] = pos
    else:
        return False
    for j in range(N):
        ret = ret or place_queen(T, (pos[0] + 1, j), queens,N,  i + 1)
    if not ret:
        queens[i] = (-1, -1)
    return ret

N = 20
T = [[0 for _ in range(N)] for _ in range(N)]
queens = [(-1, -1) for _ in range(N)]
print(place_queen(T, (0, 0), queens, N))
print(time.time()-start)