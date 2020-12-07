# . Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.
def ttf(num):
    while num > 1:
        if num % 5 == 0:
            num /= 5
        elif num % 3 == 0:
            num /= 3
        elif num % 2 == 0:
            num /= 2
        else:
            return False
    if num == 1:
        return True

n = 100
while n > 0:
    if ttf(n):
        print(n)
    n -= 1

