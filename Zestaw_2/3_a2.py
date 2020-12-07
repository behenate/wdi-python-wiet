num = 1221
s=num
rev = 0
while num > 0:
    rev *= 10
    l = num % 10
    num //= 10
    rev += l


print(s == rev)