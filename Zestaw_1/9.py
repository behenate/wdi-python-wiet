# Napisać program wypisujący podzielniki liczby.
n = 6
i = 1
while i*i < n:
    if n % i == 0:
        print(i)
    i+=1
print(n)