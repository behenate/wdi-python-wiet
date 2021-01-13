"""
Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par.
"""


def nwd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def split(num):
    def rekur_split(num, num_l, num1=0, num2=0):
        if num_l == 0:
            if num1 != 0 and num2 != 0:
                if nwd(num1, num2) == 1:
                    print(num1, num2)
                    return 1
            return 0
        new_num = num % (10 ** (num_l - 1))
        n_to_pass = num // (10 ** (num_l - 1))
        return rekur_split(new_num, num_l - 1, num1 * 10 + n_to_pass, num2) + \
            rekur_split(new_num, num_l - 1, num1, num2 * 10 + n_to_pass)

    _n = num
    nl = 0
    while _n > 0:
        _n //= 10
        nl += 1
    return rekur_split(num, nl)


print(split(21523))
