kings = [(1, 1), (2, 2)]
N = len(kings)


def check(k1, k2):
    y1, x1 = k1
    y2, x2 = k2
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    if dx == 0 or dy == 0 or dx == dy:
        return True
    return False


def all_checks(k):
    for i in range(N-1):
        for j in range(i+1, N):
            if check(k[i], k[j]):
                print(kings[i], kings[j])
                return False
    return True

print(all_checks(kings))