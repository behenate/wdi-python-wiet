from random import randint, seed

seed(3)
T = [[randint(0, 99) for _ in range(8)] for _ in range(8)]
N = len(T)

def first_digit(nuber):
    _n = nuber
    cnt = 0
    while _n > 9:
        _n //= 10
        cnt += 1
    return nuber // 10 ** cnt


def find_path(w, k):
    def place_king(a_ds, y, x, t_y, t_x, prev_move=None, i=0, p_y=0, p_x=0, path=None):
        if x < 0 or x >= N or y < 0 or y >= N:
            return False
        if first_digit(T[y][x]) <= T[p_y][p_x] % 10:
            return False
        if path is None:
            path = [-1]*(N + N)
        p = path[:]
        p[i] = prev_move
        if y == t_y and x == t_x:
            for m in p:
                if m != -1 and m is not None:
                    print(m, end=", ")
            print()
            return True

        return place_king(a_ds, y + d_t_v[a_ds[0]][0], x + d_t_v[a_ds[0]][1], t_y, t_x, a_ds[0], i + 1, y, x, p) or \
               place_king(a_ds, y + d_t_v[a_ds[1]][0], x + d_t_v[a_ds[1]][1], t_y, t_x, a_ds[1], i + 1, y, x, p) or \
               place_king(a_ds, y + d_t_v[a_ds[2]][0], x + d_t_v[a_ds[2]][1], t_y, t_x, a_ds[2], i + 1, y, x, p)

    d_t_v = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    c1 = place_king([4, 5, 6], w, k, 0, 0)
    c2 = place_king([6, 7, 0], w, k, 0, N - 1)
    c3 = place_king([0, 1, 2], w, k, N - 1, N - 1)
    c4 = place_king([2, 3, 4], w, k, N - 1, 0)
    return c1, c2, c3, c4

for line in T:
    print(line)
print("\n \n")
print(find_path(3, 2))
