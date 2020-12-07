n =

c = n
mask_length = 0
total = 0
# Sprawdzanie wymaganej długości maski
while c > 0:
    c //= 10
    mask_length += 1

for i in range(1, 2**mask_length):
    a = 2**mask_length - i  # Tutaj może być a=i ale ja printuję każdy numer 4 fun i tak mają ładniejszą kolejność
    num = 0
    c = n
    t = 0
    # Tutaj liczę która iteracja pętli jest i przeprowadzam dzielenie i modulo żeby szło w odpowiedniej kolejności.
    while a > 0:
        t += 1
        if a % 2 == 1:
            num = num * 10 + (c // 10**(mask_length-t))
        c %= 10**(mask_length-t)
        a //= 2
    if num % 7 == 0:
        total += 1


print(total)




