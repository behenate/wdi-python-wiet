n = 8

# Jako że 0<n<1000 to wygenerowanie ciągu do tablicy jest dobrym pomysłem
def fibo_do_tablicy(n):
    tab = [-1]*n
    a = 1
    b = 1
    cnt = 0
    while a < n:
        tab[cnt] = a
        c = a+b
        a = b
        b = c
        cnt += 1
    how_long = 0
    for i in range(len(tab)):
        if tab[i] != -1:
            how_long = i+1
        else:
            break
    to_ret = [0]*how_long
    for i in range(how_long):
        to_ret[i] = tab[i]
    return to_ret

tab = fibo_do_tablicy(n)
while True:
    n += 1
    can_be_rep = False
    for i in range(0, len(tab)):
        sum = 0
        while sum < n and i < len(tab):
            sum += tab[i]
            i += 1
        else:
            if sum == n:
                can_be_rep = True
                break
        if can_be_rep:
            break
    if not can_be_rep:
        print(n)
        break



