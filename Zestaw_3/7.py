"""
Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy istnieje
element tablicy zawierający wyłącznie cyfry nieparzyste.
"""
import random
top = int(input(">>"))
arr = [0]*top
for i in range(1,top+1):
    arr[i-1] = random.randint(1, 1000)

for elem in arr:
    s = elem
    while elem > 0:
        r = elem % 10
        if r % 2 == 0:
            break
        elem //= 10
    else:
        print("liczba {} jest 20z samych nieparzystych bojajże!".format(s))