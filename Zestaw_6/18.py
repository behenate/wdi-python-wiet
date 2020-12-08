"""
Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
"""
from random import randint, seed
seed(3)
T = [[randint(0, 99) for _ in range(8)] for _ in range(8)]
N = len(T)


def first_digit(nuber):
    _n = nuber
    cnt = 0
    while _n > 9:
        _n //= 10
        cnt += 1
    return nuber // 10**cnt


# Nie oceniać implementacji Path. Path jest tylko do sprawdzenia czy działa
def place_king(y=0, x=0, p_y=0, p_x=0, path=[]):
    if y == N-1 and x == N-1:
        path.append((y, x))
        print(path)
        return True
    if first_digit(T[y][x]) <= T[p_y][p_x] % 10:
        return False

    p = path[:]
    p.append((y, x))
    return place_king(y, x+1, y, x, p) or place_king(y+1, x, y, x, p) or place_king(y+1, x + 1, y, x, p)


print(place_king())
