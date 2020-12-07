l = 5
m = 7
def ile_2_5(n):
    dwojki = piatki = 0
    while n % 2 == 0:
        dwojki += 1
    while n % 5 == 0:
        piatki += 1
    return max(dwojki, piatki)

print(l//m, end="")
r = l % m
if r != 0:
    print(".", end="")
ile_przed = ile_2_5(m)
for i in range(ile_przed):
    r *= 10
    print(r//m)
    r = r % m
w_r = r
if r != 0:
    print("(", end="")
    while True:
        r *= 10
        print(r // m, end=(""))
        r %= m
        if w_r == r:
            break
    print(")", end="")