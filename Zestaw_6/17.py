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


def construct_numbers(n1, n2, n1_l, n2_l, constructed,c_l):  # num1, num2, num1_lenght, num2_length, constructed number, constructed length
    if n1_l < 0 or n2_l < 0:
        return 0
    if c_l == 0:
        print(constructed)
        if is_prime(constructed):
            print("Prime!!")
            return 1
        return 0
    added = 0
    added += construct_numbers(n1 % (10 ** (n1_l - 1)), n2, n1_l - 1, n2_l,
                               constructed + (n1 // (10 ** (n1_l - 1))) * 10 ** (c_l - 1), c_l - 1)
    added += construct_numbers(n1, n2 % (10 ** (n2_l - 1)), n1_l, n2_l - 1,
                               constructed + (n2 // (10 ** (n2_l - 1))) * 10 ** (c_l - 1), c_l - 1)
    return added


n1, n2 = 123, 75
n1_ln = n2_ln = 0

#  Liczenie długości każdej z liczb. Można ewentualnie napisać że zakłada się że liczba cyfr każdej liczby jest znana
_n1, _n2 = n1, n2
while _n1 > 0:
    _n1 //= 10
    n1_ln += 1
while _n2 > 0:
    _n2 //= 10
    n2_ln += 1

print(construct_numbers(n1, n2, n1_ln, n2_ln, 0, n1_ln + n2_ln))
