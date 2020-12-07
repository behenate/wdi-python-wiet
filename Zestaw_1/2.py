# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

start_a = 2
start_b = 2
a = 2
b = 2
found = False
year = 2020

for i in range(2, year):
    for j in range(2, year):
        start_b = j
        if j > i:
            break
        a = j
        b = i
        while a < year:
            c = a + b
            a = b
            b = c
            if a == year:
                print(j, i)
