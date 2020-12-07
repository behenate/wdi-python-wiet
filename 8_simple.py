liczba = 9
i = 3
pierwiastek = liczba**(1/2)

if liczba % 2 == 0:
    print("Nie jest")
    exit()

while i <= pierwiastek:
    if liczba % i == 0:
        print("Nie jest 1sza")
        exit()
    i += 2

print("Jest")

# 1,2,4,8,16,32,64