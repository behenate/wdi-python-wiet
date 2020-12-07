from random import randint

def copy_singleton_sort(T1, T2, N):
  ids = [0]*N
  _id = 0
  moved = 0
  while _id < N*N:
    _min = 999
    _min_id = -1
    for i in range(N):
      if ids[i] < N and T1[i][ids[i]] < _min:
        _min_id = i
        _min = T1[i][ids[i]]

    # for i in range(N):
    #   if ids[i] < N and T1[i][ids[i]] == _min:
    #     ids[i] += 1

    # for i in range(_min_id):
    #   if ids[i] < N and T1[i][ids[i]] == _min:
    #     ids[i] += 1

    # for i in range(_min_id+1, N):
    #   if ids[i] < N and T1[i][ids[i]] == _min:
    #     ids[i] += 1

    T2[_id] = T1[_min_id][ids[_min_id]]
    _id += 1

  return T2

N = int(input())
T1 = []
for i in range(N):
  T1.append(sorted([randint(-10, 10) for j in range(N)]))

for r in T1:
  print(r)
T2 = [0]*(N*N)

print(copy_singleton_sort(T1, T2, N))