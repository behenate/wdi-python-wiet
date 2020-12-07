a = 100
b = 33
n = 100

print(a//b, end=".")
a %= b
for i in range(n):
    a *= 10
    print(a//b, end="")
    a = a%b