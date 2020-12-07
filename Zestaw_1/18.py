# x^3 = a  x^3 - a = 0 f(x) = x^3-a  f'(x) = 3x^2
#
a = 64
x = a
prevx = x
while True:
    x = x - (pow(x, 3) - a) / (pow((3*x), 2))
    if(prevx == x):
        break
    prevx = x

print(round(x))