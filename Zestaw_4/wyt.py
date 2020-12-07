import time
start = time.time()
n = 10000
tab = [[0 for _ in range(n)] for _ in range(n)]

i = 0
j = 0
m_moves = n-1
print(m_moves)
moves = [1, 0, 0, 0]
m_cnt = m_moves
dir = 0
sub = 0

for l in range(n*n):
    tab[i][j] = l + 1
    j += moves[0] - moves[2]
    i += moves[1] - moves[3]
    m_cnt -= 1

    if m_cnt == 0:
        if sub % 2 == 0 and sub != 0:
            m_moves -= 1
        sub += 1
        m_cnt = m_moves
        dir = (dir+1) % 4
        moves = [0, 0, 0, 0]
        moves[dir] = 1

print(time.time()-start)