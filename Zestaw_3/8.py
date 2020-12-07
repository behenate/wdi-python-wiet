"""
Zadanie 8. Dana jest N-element tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""

def pierwsza(num):
    i = 2
    if num == 2:
        return True
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def czynniki_pierwsze(num):
    arr = []
    for i in range(2, num+1):
        if num % i == 0 and pierwsza(i):
            arr = arr + [i]
    return arr


def rekur(index=0, prev_arr=[], prev=0):
    if index < (len(pola) - 1):
        print("Prev arr:", prev_arr, "prev num:",  prev, "current array: ",tab_czynniki[index], )
    if index == cel-1:
        print("Da się!")
    if index < (len(pola)-1):
        for i, elem in enumerate(tab_czynniki[index]):
            rekur(index+elem, tab_czynniki[index], elem)


# To ma być teoretycznie generowane losowo
pola = [20, 150, 2, 200, 300, 195, 14, 15, 3, 3, 18, 21, 300, 3, 6, 3, 5, 12, 1]
cel = len(pola)

tab_czynniki = [[]]*(len(pola))

for i, elem in enumerate(pola):
    tab_czynniki[i] = czynniki_pierwsze(elem)

rekur()

