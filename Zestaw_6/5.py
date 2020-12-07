"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.
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


def to_dec(t):
    s = 0
    for i in range(len(t)-1, -1, -1):
        if t[i] == 1:
            s += 2**(len(t)-i-1)
    return s

def recur_cut(start = 0):
    num = 0
    if start == ln:
        return True
    for i in range(start, ln-1):
        num = num*2 + t[i]
        if is_prime(num) and recur_cut(i+1):
            return True
    return False
t = [1,1,0,1,0,0]
ln = len(t)
print(recur_cut())
