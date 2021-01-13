is prime, dlugosc liczy, wektory konia, samogłoski, nwd nww, palindrom,
#wektor konia:
((-1, -2), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2),(-2, 1) , (-2, -1))
# samigłoski:
a, ą, e, ę, i, o, u, y.


def nwd(a,b):
    while b!=0:
        b,a = a%b, b
    return a

def nww(a,b):
    atimesb = abs(a*b)
    return atimesb/nwd(a,b)

def calc_sum(t1, t2):
    s = sum_rows[t1[0]] + sum_cols[t1[1]] - 2*(T[t1[0]][t1[1]])

    if t1[0] != t2[0]:
        s += sum_cols[t2[1]]
        if t1[1] != t2[1]:
            s -= T[t2[0]][t1[1]]
        s -= T[t2[0]][t2[1]]

    if t1[1] != t2[1]:
        s += sum_rows[t2[0]]
        if t1[0] != t2[0]:
            s -= T[t1[0]][t2[1]]
        s -= T[t2[0]][t2[1]]
    return s

def is_prime(m):
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int((m ** (1 / 2))) + 1, 2):
        if m % i == 0:
            return False
    return True

# czynniki pierwsze
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


# PALINDROM
def reverse(num):
    reversed = 0
    while num > 0:
        reversed *= 10
        reversed += num % 10
        num //=10
    return reversed


def palindrom(num):
    if num == reverse(num):
        return True
    return False
# Koniec Palindromu

def podzielniki(num):
    dzielniki = []
    for i in range(1, int((num//2))):
        if num % i == 0:
            dzielniki = dzielniki + [i]
    return dzielniki


def sort(tab):
    for i in range(len(tab)):
        for j in range(1, len(tab)):
            if tab[j] < tab[j-1]:
                tab[j], tab[j-1] = tab[j-1], tab[j]
    return tab

def reverse_list(list):
    n = len(list)
    for i in range(0, (n//2)):
        list[i], list[n-i-1] = list[n-i-1], list[i]

