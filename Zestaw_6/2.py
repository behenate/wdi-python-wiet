"""
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool
"""

tab = [2, 3, 6, 2, 4, 1]
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

def waga(num):
    cnt = 0
    i = 2
    while num > 1:
        if num % i == 0:
            cnt += 1
            while num%i == 0:
                num //= i
        i += 1
    return cnt


def da_sie(i=0, s1=0, s2=0, s3=0):
    if i == len(tab) :
        if s1 == s2 and s2 == s3:
            return True
        else:
            return False
    return da_sie(i+1, s1+tab[i], s2, s3) or da_sie(i+1, s1, s2+tab[i], s3) or da_sie(i+1, s1, s2, s3+tab[i])


print(da_sie())