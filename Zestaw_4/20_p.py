import time
import random
start = time.time()
def two_rooks_max_check_sum(T, N):
  cols_sums = [0]*N
  rows_sums = [0]*N

  for x in range(N):
    for y in range(N):
      cols_sums[x] += T[y][x]
      rows_sums[x] += T[x][y]

  _max_sum = -1
  _max_coords = [-1, -1, -1, -1]
  for x1 in range(N):
    for y1 in range(N):
      for x2 in range(x1, N):
        for y2 in range(N):
          if x1 != x2 and y1 != y2:
            ms = [x1 != x2, y1 != y2]
            _sum = ms[0]*rows_sums[x1] + rows_sums[x2] + ms[1]*cols_sums[y1] + cols_sums[y2] - (2*T[x1][y1] + 2*T[x2][y2] + (ms[0]+ms[1])//2*T[x1][y2] + (ms[0]+ms[1])//2*T[x2][y1])

            if _sum > _max_sum:
              _max_sum = _sum
              _max_coords = [x1, y1, x2, y2]

  return (_max_sum, _max_coords)


N = 8
random.seed(0)
T = [[random.randint(0,9) for _ in range(20)] for _ in range(20)]
print(T)
print(two_rooks_max_check_sum(T, N))
print(time.time()-start)
