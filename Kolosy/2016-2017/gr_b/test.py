def dec_to_bin(x):
    bin = 1
    while x > 1:
        bin = bin * 10 + x % 2
        x //= 2

    return bin
def dec_to_bin1(n):
    bin = 1
    while n > 1:
        bin *= 10
        bin += n%2
        n//=2
    return bin
def dec_to_bin2(n):
    bin = 0
    i = 1
    while n > 0:
        bin = bin + (n%2)*i
        n //= 2
        i*=10
    return bin
print (dec_to_bin2(14))