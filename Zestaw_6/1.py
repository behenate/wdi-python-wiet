"""
Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry
"""
def is_prime(n):
    if n <=1:
        return False
    if n ==2 or n ==3:
        return True
    if n %2==0 or n % 3==0:
        return False
    i = 6
    while (i-1)**2 <= n:
        if n %(i-1) == 0:
            return False
        if n%(i+1) == 0:
            return False
        i+=6
    return True

def usun(liczba, liczba_cyfr, nr_cyfry):
    if liczba_cyfr == 1:
        res = is_prime(liczba)
        if res:
            secik.add(liczba)
            return True
    else:
        a = liczba // 10**(nr_cyfry)
        b = liczba % 10**(nr_cyfry-1)
        c = a*10**(nr_cyfry-1) + b
        for i in range(1, liczba_cyfr + 1):
            usun(c, liczba_cyfr - 1, i)


liczba = 12345
liczba_cyfr = 5
secik = set()
for i in range(1, liczba_cyfr):
    usun(liczba, liczba_cyfr-1, i)
print(secik)