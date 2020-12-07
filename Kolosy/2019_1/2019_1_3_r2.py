
def kings(x,y, tab, s, k1):
    N = len(tab)
    dasie = False
    if y == N:
        if s == 0:
            return True
    else:
        for n in range(N):
            dasie = kings(n, y, tab, s, k1)

        if abs(x-k1) >= 2:
            dasie = kings(0, y+1, tab, s+tab[y][x], x)
        if dasie:
            return dasie

tab = [
    [ 1,  0,  0,  0,  0,  0,  0],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5]
]
print(kings(0, 0, tab, 0, -2))