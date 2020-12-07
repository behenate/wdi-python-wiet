t1 = [2, 3, 0, 1]
t2 = [1, 4, 0, 5]

ln = len(t1)
n = 2**len(t1)

max_sum = 0
for i in range(1, n):
    s = 0
    cnt = 0
    _n = i
    j = 0
    while _n > 0:
        if _n % 2 == 1:
            s += t1[j]
            cnt += 1
        j += 1
        _n //= 2
    for k in range(1, n):
        s1 = 0
        cnt1 = 0
        _n = k
        j = 0
        while _n > 0:
            if _n % 2 == 1:
                s1 += t2[j]
                cnt1 += 1
            j += 1
            _n //= 2

        if s == s1 and cnt == cnt1:
            if cnt1 > max_sum:
                max_sum = cnt1

print(max_sum)
