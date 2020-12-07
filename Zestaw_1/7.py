# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

s = int(input("Podaj liczbę naturalną: "))

a = 1
b = 1
while a < s:
    if s == a*b:
        print("Jest {}*{}".format(a, b))
        exit()

    else:
        c = a+b
        a=b
        b=c

print("Nie jes")