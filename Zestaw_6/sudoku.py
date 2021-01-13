from random import randint, seed
seed(0)
def convert_to_5(num):
    _n = num
    l = 0
    while _n > 0:
        _n //= 5
        l += 1
    t = [-1]*l
    for i in range(l):
        t[len(t)-i-1] = num%5
        num //= 5
    return t

def compare(y, x, t1, t2, l1, l2):
    comp_cnt = 0
    match_cnt = 0
    for c_y in range(l2):
        if y+c_y < 0 or y+c_y >= l1:
            continue
        for c_x in range(l2):
            if x + c_x < 0 or x + c_x >= l1:
                continue
            comp_cnt += 1
            if convert_to_5(t1[y+c_y][x+c_x]) == convert_to_5(t2[c_y][c_x]):
                match_cnt += 1
    if match_cnt == comp_cnt:
        return 0
    return match_cnt/comp_cnt



max1 = 8
max2 = 3
tab1 = [[randint(0,9) for _ in range(max1)] for _ in range(max1)]
tab2 = [[randint(0,9) for _ in range(max2)] for _ in range(max2)]

for y in range(-max2, max1+max2):
    for x in range(-max2, max1+max2):
        res = compare(y,x, tab1, tab2, max1, max2)
        if res >= 0.33:
            print(res, y, x)

for line in tab2:
    print(line)
for line in tab1:
    print(line)