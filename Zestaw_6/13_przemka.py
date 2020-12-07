from time import time
start = time()
def func(n, p, last):
  if n == 0:
    print(p)

  for i in range(last, n+1):
    func(n-i, p+f'{i} ', i)


n = 20
func(n, '', 1)
print(time()-start)