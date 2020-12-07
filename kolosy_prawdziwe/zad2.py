#Wojciech Dróżdż
from copy import deepcopy
T = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1]

]

def distance(T):
    T1 = deepcopy(T)
    print(T1)
    N = len(T)
    for i in range(N):
        for j in range(0, N - i - 1):
            for a in range(N):
                if T1[j][a] > T1[j+1][a]:
                    T1[j+1], T1[j] = T1[j], T1[j+1]
                    break
                elif T1[j+1][a] > T1[j][a]:
                    break

    min = T1[0]
    max = T1[N-1]
    min_index = 0
    max_index = 0
    print(T1)
    for i in range(N):
        if T[i] == min:
            min_index = i
            break
    print(min_index)
    for i in range(N):
        if T[i] == max:
            max_index = i
            break

    return abs(max_index - min_index)

print(distance(T))