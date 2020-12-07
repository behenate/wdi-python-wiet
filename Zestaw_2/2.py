# Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
# ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

a = 6
b = 7
n = 100
print(a // b, end="")
a = a % b
print(".", end="")
while n > 0:
    if a < b:
        a *= 10
        print(a // b, end="")
        a = a % b
    else:
        print(a // b, end="")
        a = a % b
    n -= 1