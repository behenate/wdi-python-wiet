# . Napisać program sprawdzający czy zadana liczba jest pierwsza.
liczba =  5000101
if liczba % 2 == 0:
    exit("Nie jest pierwsza")

for i in range(2, liczba//2):
    print("Przeanalizowano {}% liczby".format(float((i*100/liczba))*2))
    if liczba % i == 0:
        exit("Nie jest pierwsza")

print("Jest pierwsza :*")