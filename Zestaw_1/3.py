# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie

# 1,1,2,3,5,8,13,21
szukana_suma = 8
s_a = 1
s_b = 1
a = s_a
b = s_b
suma = 0
found = False
while s_a < szukana_suma:
    while a < szukana_suma:
        suma += a
        c = a+b
        a = b
        b = c
        if suma == szukana_suma:
            found = True
            break
    if found:
        break
    s_c = s_a+s_b
    s_a = s_b
    s_b = s_c
    a = s_a
    b = s_b
    suma = 0
print(found)