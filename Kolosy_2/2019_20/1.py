from random import randint, seed
seed(0)
def num_even(num):
    _n = num
    l = 0
    while _n > 0:
        _n //= 5
        l += 1
    even_cnt = 0
    for i in range(l):
        if (num % 5) % 2 == 0:
            even_cnt += 1
        num //= 5
    return even_cnt

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
            if t1[y+c_y][x+c_x] == t2[c_y][c_x]:
                match_cnt += 1
            print("y:{} x:{} cy:{} cx:{}, curr%={} ".format(y,x,c_y,c_x, match_cnt/comp_cnt))
    if comp_cnt == 0:
        return 0
    return match_cnt/comp_cnt



max1 = 8
max2 = 3
tab1 = [[randint(0, 1) for _ in range(max1)] for _ in range(max1)]
tab2 = [[randint(3, 200000000000000) for _ in range(max2)] for _ in range(max2)]

for y in range(max1):
    for x in range(max1):
        tab1[y][x] = num_even(tab1[y][x])

for y in range(max2):
    for x in range(max2):
        tab2[y][x] = num_even(tab2[y][x])


for y in range(-max2, max1+max2):
    for x in range(-max2, max1+max2):
        res = compare(y, x, tab1, tab2, max1, max2)
        if res >= 0.33:
            # print(res, y, x)
            continue

for line in tab2:
    print(line)
for line in tab1:
    print(line)