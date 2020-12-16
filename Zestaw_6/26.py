"""
Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2), 10100(2), 11000(2)
"""


def binary_to_dec(num):
    n = len(num)
    dec = 0
    for i in range(n-1, -1, -1):
        dec += (2**i) * num[n-i-1]
    return dec


def is_prime_binary(num):
    dec = binary_to_dec(num)
    if dec < 2:
        return False
    if dec == 2:
        return True
    if dec % 2 == 0:
        return False
    for i in range(3, int(dec**(1/2))+1):
        if dec % i == 0:
            return False
    return True


def binary_generator(num, a_left, b_left):
    if a_left < 0 or b_left < 0:
        return 0
    if a_left == 0 and b_left == 0 and not is_prime_binary(num):
        print(num)
        return 1
    total = 0
    total += binary_generator(num+[1], a_left-1, b_left)
    if len(num) != 0:
        total += binary_generator(num+[0], a_left, b_left-1)
    return total


print(binary_generator(list(), 2, 3))