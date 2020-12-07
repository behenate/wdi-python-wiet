def nwd(a,b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

def nwd1(a,b):
    while b!=0:
        b,a = a%b, b
    return a
print(nwd1(9, 81))
