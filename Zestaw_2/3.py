# Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

# def palindrom(p, binary=False):
#     s_p = str(p)
#     if binary:
#         s_p = bin(s_p)
#         s_p = s_p[2:]
#     r_p = ""
#     c = len(s_p)
#     while c > 0:
#         r_p += s_p[c - 1]
#         c -= 1
#     if s_p == r_p:
#         print("Jest")
#         return True
#     print("Nie jest")
#     return False
#
#
# palindrom(1221)
"""
1234
4
>>1

"""
num = 1234


def len_num(num)
    len = 0
    while num > 1:
        num /= 10
        len += 1
    # end while
    return len
"""
1234 
/10 bez reszty * 10 to jest 1230
pierwsza cyfra odwrotnosci 4


123

"""

def reverse(num):
    reversed = 0
    while num > 0:
        reversed *= 10
        bez_reszty = num//(10)*10
        r = num % 10
        reversed += r
        num = bez_reszty//10
    return reversed


def palindrom(num):
    if num == reverse(num):
        return True
    return False

print(palindrom(11011))

