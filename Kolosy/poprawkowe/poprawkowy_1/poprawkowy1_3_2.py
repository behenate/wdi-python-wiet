import time
start = time.time()
t1 = [i for i in range(10000)]
t2 = [i+3 for i in(range(10000))]
n1 = len(t1)
n2 = len(t2)

t3 = [-1]*min(n1, n2)
i = j = k = 0
try:
  while True:
    while t1[i] < t2[j]:
      i += 1

    if t1[i] == t2[j]:
      t3[k] = t1[i]
      i += 1
      j += 1
      k += 1

    while t2[j] < t1[i]:
      j += 1
except IndexError:
  pass

for e in t3:
  if e == -1:
    break
  print(e, end=' ')
print(time.time()-start)