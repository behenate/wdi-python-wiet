"""

Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie

"""


def add(z1, z2):
    return z1[0]+z2[0], z1[1]+z2[1]


def sub(z1, z2):
    return add(z1, (-z2[0], -z2[1]))


def multi(z1, z2):
    re = (z1[0]*z2[0]) - (z1[1]*z2[1])
    im = (z1[1]*z2[0]) + (z1[0]*z2[1])
    return (re, im)

def div(z1,z2):
    z1 = multi(z1, (z2[0], -z2[1]))
    z2 = multi(z2, (z2[0], -z2[1]))
    return z1[0]/z2[0], z1[1]/z2[0]

def pow(z1, n):
    temp = z1
    if n == 0:
        return 1
    for i in range(n-1):
        z1 = multi(z1, temp)
    return z1

def read_num():
    re = int(input("Podaj część rzeczywistą >> "))
    im = int(input("Podaj część urojoną >> "))
    return re, im
def print_num(n):
    s = "-" if n[1] < 0 else "+"
    print("{} {} {}i".format(n[0], s, abs(n[1])))
