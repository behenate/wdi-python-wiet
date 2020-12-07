kings = [(1, 1), (2, 2)]
N = 3
t = [[0 for _ in range(2*N-1)] for _ in range(4)]
for i, king in enumerate(kings):
    t[0][king[1]] = t[0][king[1]] + 1
    t[1][king[0]] = t[1][king[0]] + 1
    t[2][(king[1]-king[0])+(N-1)] = t[2][(king[1]-king[0])+(N-1)] + 1
    t[3][king[0]+king[1]] = t[3][king[0]+king[1]] + 1

for i in range(4):
    for j in range(2*N-1):
        if t[i][j] > 1:
            print("Kolizja!")
            break

