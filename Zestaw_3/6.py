"""
Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000
i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""
import random
top = int(input(">>"))
arr = [0]*top
for i in range(1,top+1):
    arr[i-1] = random.randint(1,1000)

for elem in arr:
    s = elem
    while elem > 0:
        r = elem % 10
        if r % 2 == 1:
            print("liczba {} posiada cyfrę nieparzystą!".format(s))
            break
        elem //= 10
    else:
        print("liczba {} nie posiada cyfry nieparzystą!".format(s))