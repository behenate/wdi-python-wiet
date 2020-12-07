t1 = [i for i in range(10000)]
t2 = [i+3 for i in(range(10000))]
n1 = len(t1)
n2 = len(t2)

t3 = [-1]*min(n1, n2)
k = i = j = 0

while i < n1-1 and j < n2-1:
    while t1[i] < t2[j] and i < n1-1 and j < n2-1:
        i += 1
    if t1[i] == t2[j]:
        t3[k] = t1[i]
        i += 1
        j += 1
        k += 1

    while t2[j] < t1[i] and i < n1-1 and j < n2-1:
        j += 1

for e in t3:
    if e == -1:
        break
    print(e, end=' ')
