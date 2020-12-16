"""
Zadanie 15. Problem 8 Hetmanów (treść oczywista)
"""
import time
start = time.time()

def can_place(pos, queens):
    for y, queen in enumerate(queens):
        if queen == -1:
            break
        x = queen
        diff = y - x
        sum = y + x
        if pos[0] == y or pos[1] == x or pos[0] - pos[1] == diff or pos[0] + pos[1] == sum:
            return False
    return True


def place_queen(pos, queens, N, i=0):
    ret = False
    if pos[0] == N:
        print(queens)
        return True
    if can_place(pos, queens):
        queens[i] = pos[1]
    else:
        return False
    for j in range(N):
        ret = ret or place_queen((pos[0] + 1, j), queens, N,  i + 1)
    if not ret:
        queens[i] = -1
    return ret

N = 8
queens = [-1 for _ in range(N)]
print(place_queen((0, 0), queens, N))
print(time.time()-start)