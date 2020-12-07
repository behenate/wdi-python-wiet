start_a = 1
start_b = 1
a = 1
b = 1
found = False

while not found:
    start += 1
    a = start
    b = start
    while True:
        c = a + b
        a = b
        b = c
        if a == 1919:
            found = True
            break
        if a > 1919:
            break
    if found:
        break
print(a, start)