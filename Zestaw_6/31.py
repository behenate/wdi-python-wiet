import time
start = time.time()
def is_prime(m):
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int((m**(1/2)))+1, 2):
        if m % i == 0:
            return False
    return True


def find_primes(num, T):
    cnt = 0
    if num %2 == 0:
        T[0] = 2
        cnt += 1

    for i in range(3, int(num**(1/2))+1, 2):
        if is_prime(i) and num%i == 0:
            T[cnt] = i
            cnt += 1
    print("FOUND THE PRIMES BRUHHHHH")


def factorize(T, m):
    cnt = 0
    i = 2
    while m > 1:
        f = False
        while m % i == 0:
            f = True
            m //= i
        if f:
            T[cnt] = i
            cnt += 1
        i += 1

def calculate(T, calc, i):
    if i == len(T):
        if calc == 1:
            return 0
        return calc
    res = 0
    res += calculate(T, calc*1, i+1)
    res += calculate(T, calc*T[i], i+1)

    return res


tab = [-1]*25
factorize(tab, 2305567963945518424753102147331756070)
print(tab)
t_l = 0
for elem in tab:
    if elem == -1:
        break
    t_l += 1
n_tab = [0]*t_l

for i in range(t_l):
    n_tab[i] = tab[i]

print(calculate(n_tab,1,0))
print(time.time()-start)