# Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
a = 1
b = 1


def quovadis(x,y):
    for i in range(50):
        c = x + y
        x = y
        y = c
    return (y / c)

q = quovadis(1,1)

for i in range(2,1000):
    for j in range(2,1000):
        if j > i:
            break
        if quovadis(j, i) == q:
            print(j, i)

print(quovadis(846,999), q)