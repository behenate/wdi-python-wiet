a = 1
b = 1
c = 1
l = 0
n = 10**100

while c < n:
    b = c
    while b < n:
        a = b
        while a < n:
            l += 1
            a *= 2
        b *= 2
    c *= 5
print(l)