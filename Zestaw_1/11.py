# Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

for j in range(1, 1000000):
    sum = 0

    for i in range(1, (j//2)+1):
        if j % i == 0:
            sum += i
    for k in range(1, j-1):
        sum1 = 0
        for l in range(1, (k//2)+1):
            if k % l == 0:
                sum1 += l
        if sum1 == j and sum == k:
            print("{} i {}".format(j, k))




# 1 liczba 1 -1000000
# 2 dzielniki tej liczby
# Kiedy są już dzielniki lecimy przez każdą liczbe mniejsza od tej i szukamy jej dzielników wszystkich