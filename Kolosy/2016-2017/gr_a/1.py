"""
Dane są dwa ciągi określone następująco:
a1 = 1 an = an−1 + bn/3
b1 = 2 bn = bn−1 + an−1
Proszę napisać program, który wczytuje liczbę naturalną k i odnajduje wyraz należący do
jednego z ciągów o wartości najbliższej k. Program powinien wypisać numer znalezionego
wyrazu i ciąg z którego on pochodzi. Jeżeli więcej niż jeden wyraz jest jednakowo odległy
od k, należy wybrać ten o mniejszym numerze

"""

def ciag(an, bn,k, prev, p_diff, n=1):
    bn1 = bn + an
    an1 = an + bn1/3

    da = abs(an1 - k)
    db = abs(bn1 - k)
    if da < db and da < p_diff:
        res = ciag(an1, bn1, k, "a", da, n+1)
    elif db < da and db < p_diff:
        res = ciag(an1, bn1, k, "b", db, n+1)
    else:
        res = prev+str(n)
    return res

k = -1000
print(ciag(1, 2, k, "b", abs(2-k)))
