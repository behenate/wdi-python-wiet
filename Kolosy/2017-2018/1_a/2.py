import random
N = 8

tab = [0, 1, 2, 3, 4, 3, 6, 7]
max_len = 0
i = 0
while i <= (N-1):
    index_sum = i
    sum = tab[i]
    prev = tab[i]
    ln = 1
    for j in range(i+1, N):
        if tab[j] > prev:
            prev = tab[j]
            sum += tab[j]
            index_sum += j
            ln += 1
            i = j-1
        else:
            if index_sum == sum and ln > max_len:
                max_len = ln
                break
    if index_sum == sum and ln > max_len:
        max_len = ln
    i += 1
print(max_len)