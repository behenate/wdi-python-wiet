
liczba = 16

# dla 1, 2,
i = 2
# Dla 16:   1,2,4,8,16,32,64
while i*i < liczba:
    if liczba % i == 0:
        break
    i += 1

if i*i >= liczba:
    print("Jest?")
else:
    print("Nie jest")

