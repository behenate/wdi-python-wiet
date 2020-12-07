"""
Dane są ciągi an, bn i cn określone następująco:
an = 1 dla n = 1, 2 bn = 1 dla n = 1, 2, 3
an = an−1 + an−2 dla n > 2 bn = bn−1 + bn−2 + bn−3 dla n > 3
Wyrazy ciągu cn są kolejnymi liczbami naturalnymi należącymi do ciągu an lub bn.
Ciągi te przyjmują wartości:
an : 1 1 2 3 5 8 13 21 ...
bn : 1 1 1 3 5 9 17 31 ...
cn : 1 2 3 5 8 9 13 17 ...
Proszę napisać program który w Proszę napisać program który wczytuje wprowadzoną z klawiatury liczbę naturalną k
i wypisuje k-ty wyraz ciągu cn.
"""

k = 100
a1 = a2 = 1
a = [1, 2]
b1 = b2 = b3 = 1
c = [0]*k
c[0] = a1
count = 1
for i in range(k):
    an = a1 + a2
    bn = b1 + b2 + b3
    if an > bn:
        c[count] = bn
        count += 1
        b3 = b2
        b2 = b1
        b1 = bn
    elif bn > an:
        c[count] = an
        count += 1
        a3 = a2
        a2 = a1
        a1 = an
    else:
        a3 = a2
        a2 = a1
        a1 = an
