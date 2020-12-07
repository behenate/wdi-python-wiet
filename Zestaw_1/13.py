import time
# Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.
ia = 64
ib = 16
ic = 8
a = ia
b = ib
c = ic
while True:
    if a == b and c == b:
        print("NWW: {}".format(a))
        break
    s = min(a,b,c)

    if a == s:
        a += ia
    elif b == s:
        b += ib
    else:
        c += ic
