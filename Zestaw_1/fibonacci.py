a = 2014
b = 3
while a < 1000000:
    c = a + b
    a = b
    b = c
    if a < 1000000:
        print(a)