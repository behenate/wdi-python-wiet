# Wojciech Dróżdż
# Algorytm dla każdego możliwego elementu mniejszego od siebie sprawdza czy jego długość jest wielokrotnością
# Innego elementu. Jeżeli tak to przemnaża on ten element przez wielokrotność. Jeżeli inny element jest teraz równy
# Sprawdzanemu to jeżeli ta długość jest dłuższa od najdłuższej dotąd zarejestrowanej to przypisuje on ją do zmiennej
# Na końcu zwraca on najdłuższą zarejestrowaną długość
# Algorytm można znacznie przyspieszyć sortując tablicę od najdłuższego elementu, wtedy pierwszą znalezioną wielokrotność
# można by od razu zwrócić.
def multi(T):
    N = len(T)
    max_len = 0
    for i in range(N):
        curr = T[i]
        l_curr = len(curr)
        for j in range(N):
            check = T[j]
            l_c = len(check)
            if check != T[i] and l_curr > l_c and l_curr % l_c == 0:
                check *= l_curr//l_c
                if check == curr:
                    if l_curr > max_len:
                        max_len = l_curr
    return max_len