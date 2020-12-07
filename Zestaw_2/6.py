num = int(input(">>"))
mid = num**(1/2)

if int(mid) == mid:
    b = t = int(mid)
elif int(mid) % 2 > 0.5:
    b = int(mid)
    t = int(mid)+1
else:
    b = int(mid)
    t = int(mid)+2

print(b, t)