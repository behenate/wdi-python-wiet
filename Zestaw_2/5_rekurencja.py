n = 2315
mod = 7

_n = n
digits = 0
while _n > 0:
  n = (n*10 + _n%10)
  _n //= 10
  digits += 1
n %=10**digits
print(n)

