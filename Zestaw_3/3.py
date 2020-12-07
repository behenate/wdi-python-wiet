"""
Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
"""

n = 1000
arr = [True]*n
i=2
while i*i < n:
    if arr[i]:
        for j in range(i*i, n, i):
            arr[j] = False
    i += 1

for i in range(len(arr)):
    if arr[i]:
        print(i)
