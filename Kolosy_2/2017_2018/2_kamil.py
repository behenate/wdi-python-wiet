tablica = [3]


def czypierwsza(liczba):
    if (liczba == 2 or liczba == 3 or liczba == 5 or liczba == 7):
        return True
    else:
        return False


flaga = 0


def rekur(tab, n=1):
    global flaga
    liczba = tab[n - 1]
    if (n == 9):
        print(tab)
        flaga += 1
        return "chuj"
    for i in range(1, 10):
        if ((i not in tab) and abs(liczba - i) >= 2 and not (czypierwsza(liczba) and czypierwsza(i))):
            tabx = tab[:]
            tabx.append(i)
            rekur(tabx, n + 1)


rekur(tablica)
print(flaga)
