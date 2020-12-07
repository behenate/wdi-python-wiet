def to_system(num, n):
    _n = num
    l = 0
    while _n > 0:
        _n //= n
        l += 1
    to_ret = [0]*l

    for i in range(l-1, -1, -1):
        to_ret[i] = num % n
        num //= n
    return to_ret


def in_array(arr, elem):
    for e in arr:
        if e == elem:
            return True
    return False


def roznocyfrowe(arr_num, arr_num2):
    found_1 = [-1]*len(arr_num)
    cnt = 0
    for e in arr_num:
        if in_array(arr_num2, e):
            return False
    return True


def znajdz(num1, num2):
    for i in range(2, 17):
        if roznocyfrowe(to_system(num1, i), to_system(num2,i)):
            return i
    return False

print(znajdz(123, 522))
