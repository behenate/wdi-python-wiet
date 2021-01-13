from random import randint


def inc_sum(t, rooks):
    N = len(t)

    def check_sums(t, N):
        row_sums = [0] * N
        col_sums = [0] * N
        for row in range(N):
            for col in range(N):
                row_sums[row] += t[row][col]

        for col in range(N):
            for row in range(N):
                col_sums[col] += t[row][col]

        return (row_sums, col_sums)

    row_sums, col_sums = check_sums(t, N)
    print(row_sums, col_sums)
    def move_rook(t, N, row_sums, col_sums, rook_s):
        _max_sum = 0
        _max_ids = [-1, -1]
        for row in range(N):
            for col in range(N):
                if row == rook_s[0] and col == rook_s[1]:
                    continue
                _sum = row_sums[row] + col_sums[col]
                _sum -= t[row][col] + t[rook_s[0]][rook_s[1]]
                if row == rook_s[0]:
                    _sum += col_sums[rook_s[1]]
                elif col == rook_s[1]:
                    _sum += row_sums[rook_s[0]]
                else:
                    _sum += row_sums[rook_s[0]] + col_sums[rook_s[1]]

                if _sum > _max_sum:
                    _max_sum = _sum
                    _max_ids = [row, col]

        return (_max_sum, _max_ids)

    rook1 = move_rook(t, N, row_sums, col_sums, rooks[0])
    rook2 = move_rook(t, N, row_sums, col_sums, rooks[1])
    print(rook1, rook2)


N = 8
rr = (0, 0)
t = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]
rooks = ((0, 0), (3, 3))
t[0][N - 1] = 100

for r in t:
    print(r)
inc_sum(t, rooks)
