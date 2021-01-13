"""
2. Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji.
"""


def A(num):
    return num+3


def B(num):
    return num*2

def C(num):
    _n = num
    n_l = 0
    ret_num = 0
    while _n > 0:
        _n //= 10
        n_l += 1
    for i in range(n_l):
        f_d = num // (10 ** (n_l - i - 1))
        num %= (10 ** (n_l - i - 1))
        if f_d % 2 == 0:
            f_d += 1
        f_d *= (10 ** (n_l - i - 1))
        ret_num += f_d
    return ret_num
def C_na_tablicy(num):
    _n = num
    n_l = 0
    while _n > 0:
        _n //= 10
        n_l += 1
    _n = num
    ret_num = [0]*n_l
    for i in range(n_l):
        if (_n%10) % 2 ==0:
            ret_num[i] = (_n % 10) + 1
        else:
            ret_num[i] = _n % 10
        _n //= 10
    to_ret = 0
    for i in range(n_l):
        to_ret *= 10
        to_ret += ret_num[-i-1]
    return to_ret
print(C_na_tablicy(1234))


def trasform(x,y,n, path=""):
    if len(path) > n:
        return 0
    if x == y:
        print(path)
        return 1
    ret_num = 0
    if path == "" or path[-1] != 'A':
        ret_num += trasform(A(x), y, n, path+'A')
    if path == "" or path[-1] != 'B':
        ret_num += trasform(B(x), y, n, path+'B')
    if path == "" or path[-1] != 'C':
        ret_num += trasform(C(x), y, n, path+'C')
    return ret_num

# print(trasform(11, 31, 4))

