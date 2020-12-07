# Proszę napisać program rozwiązujący równanie x
# xpow(x) = 2020 metodą bisekcji
# xpow(x) - 2020 = 0


number = 2029


a = 0
b = 20


while True:
    x0 = (a+b)/2
    if pow(a, a) > 2020:
        b = x0
    else:
        a = x0
    if abs(a-b) < 0.000001:
        print(a)
        break