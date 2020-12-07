# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

number = 36
precision = 10000
a = 1
b = number
i = 0
while i < precision:
    i += 1
    a = (a+b)/2
    b = number/a
print(a)