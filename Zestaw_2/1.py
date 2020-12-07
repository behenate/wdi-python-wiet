# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

class Fibo:
    def __init__(self):
        self.x = 1
        self.y = 1

    def next(self):
        c = self.x
        self.x = self.y
        self.y = self.y + c


liczba = input("Lol podaj liczbe typie")
f_a = Fibo()
f_b = Fibo()

for i in range(liczba):
    for j in range(liczba):
        if liczba == (f_a.x * f_b.x):
            print("Jest")
            exit()
        f_a.next()
    f_a.x = 1
    f_a.y = 1
    f_b.next()

print("Nie jest")