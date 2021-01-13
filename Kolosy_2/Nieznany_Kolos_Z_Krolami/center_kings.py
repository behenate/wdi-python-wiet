N = 7
T = [[0 for _ in range(N)] for _ in range(N)]
center = (N//2, N//2)

kings = [(0,0), (6,6),(4,5),(3,2),(3,1),(6,1), (1,6)]

for line in T:
    print(line)


def count_moves(pos, center):
    y, x = pos[0], pos[1]
    d_y = abs(center[0] - y)
    d_x = abs(center[1] - x)
    return max(d_y, d_x)
for x in range(N):
    for y in range(x+1, N):
        if count_moves(kings[x], center) == count_moves(kings[y], center):
            print(kings[x], kings[y])
            break
print(count_moves((3,2),(3,3)))