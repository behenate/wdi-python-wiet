"""
Zadanie 4. Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

"""

import time
start = time.time()



def exact_div(num1, num2, len):
    przed = num1 // num2
    po = 0
    for i in range(len):
        num1 *= 10
        po = po*10 + num1//num2
        num1 %= num2
    return [przed, po]


def exact_sum(num1, num2, len):
    przed = num1[0] + num2[0]
    po = num1[1] + num2[1]
    po += przed//10**len
    po %= 10**len
    return [przed, po]


total = [0, 0]
length = 10000
prev = [0,0]
i = 0
silnia = 1
# Generalnie to sposób działa spoko ale 3 ostatnie liczby zawsze są źle więc dodaję 10 do długości a potem w princie
# usuwam nadmiar.
while True:
    to_add = exact_div(1, silnia, length+10)
    total = exact_sum(total, to_add, length+10)
    if prev[0] == total[0] and prev[1]//10*7 == total[1]//10*7:
        break
    prev = total
    i += 1
    silnia *= i

print("{}.{}".format(total[0], total[1]//10**10))
print("W czasie: {}".format(time.time()-start))