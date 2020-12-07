# Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb
a = 75
b = 100
c = 25

max = 1
for i in range(1, min(a,b,c)+1):
    if a % i == 0 and b % i == 0 and c %i == 0:
        max = i if i > max else max
print(max)
