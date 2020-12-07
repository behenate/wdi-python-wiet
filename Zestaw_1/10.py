# Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
n = 1000000
sum = 0
for j in range(1, n+1):
    for i in range(1, (j//2)+1):
        if j % i == 0:
            sum += i

    if sum == j:
        print(sum)
    sum = 0
