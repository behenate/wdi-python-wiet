

import time
start = time.time()
# MAX=n = 200
# T1 = [[i+(j*MAX) for i in range(MAX)] for j in range(MAX)]
# T2 = [0 for _ in range(MAX*MAX)]
T1 = [
    [3, 4, 5],
    [1, 2, 2],
    [1, 10, 20]
]
n = len(T1)
T2 = [0]*(n*n)
for i in range(n):
    for j in range(n):
        for k in range((n**2)-1, -1, -1):
            if T1[i][j] > T2[k]:
                t1 = T2[1:k+1]
                t2 = T2[k+1:]
                T2 = t1 + [T1[i][j]] + t2
                break
            elif T1[i][j] == T2[k]:
                break
print(T2)
print(time.time()-start)