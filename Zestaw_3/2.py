"""
Zadanie 2. Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
"""

a, b = 11121, 22221
digits = [0]*10

while a > 0:
  digits[a%10] += 1
  a //= 10

while b > 0:
  digits[b%10] -= 1
  b //= 10

for i in range(10):
  if digits[i] != 0:
    print('no')
    break
else:
  print('yes')