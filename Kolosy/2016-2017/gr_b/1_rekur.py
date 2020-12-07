k = 996
a = [1, 1]
b = [1, 1, 1]
c = [0]*k
c[0] = 1

def rekur(a, b, c, id):
    if id == len(c)-1:
        return c
    an = a[0] + a[1]
    bn = b[0] + b[1] + b[2]
    if an >= bn:
        if c[id] != bn:
            id += 1
            c[id] = bn
        res = rekur(a, [bn, b[0], b[1]], c, id)
    else:
        if c[id] != an:
            id += 1
            c[id] = an
        res = rekur([an, a[0]], b, c, id)
    return res

print(rekur(a, b, c, 0))