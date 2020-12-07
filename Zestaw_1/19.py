# Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3!
e = 0
s = 1

i = 1
prev_e = 0
while True:
    e += 1/(s)

    if(e == prev_e):
        break
    s *= i
    i += 1
    prev_e = e
print(e)