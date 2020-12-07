n = 5000101
i = 2

while i*i < n:
  if n % i == 0:
    break
  i += 1
if i*i >= n:
  print('prime')
else:
  print('not prime')