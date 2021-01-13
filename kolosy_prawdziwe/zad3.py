# Wojciech Dróżdż
# Są 2 funkcje pomocnicza calc_value zliczająca wartośc pól szachowanych przez wieże oraz funkcja chess która
# Przechodząc po wszydtrkich możliwych kombinacjachpozycji  szuka wartości dla której suma jest największa i zwraca
# Ta pozycję


def calc_value(T, pos1, pos2, n):
    sum = 0
    for y1 in range(n):
        if y1 == pos1[0]:
            continue
        sum += T[y1][pos1[1]]

    for x1 in range(n):
        if x1 == pos1[1]:
            continue
        sum += T[pos1[0]][x1]

    for y2 in range(n):
        if pos2[1] == pos1[1]:
            sum -= T[pos2[0]][pos2[1]]
            break
        if y2 == pos2[0] or y2 == pos1[0]:
            continue
        sum += T[y2][pos2[1]]

    for x2 in range(n):
        if pos2[0] == pos1[0]:
            sum -= T[pos2[0]][pos2[1]]
            break
        if x2 == pos2[1] or x2 == pos1[1]:
            continue
        sum += T[pos2[0]][x2]
    return sum


def chess(T):
    n = len(T)
    max_sum = -9999999999999999999
    my1, mx1, my2, mx2 = 0, 0, 0, 0
    for y1 in range(n):
        for x1 in range(n):
            for y2 in range(n):
                for x2 in range(n):
                    if y1 != y2 and x1 != x2:
                        res = calc_value(T, (y1,x1), (y2,x2), n)
                        if res > max_sum:
                            my1, mx1, my2, mx2 = y1, x1, y2, x2
                            max_sum = res
    return (my1,mx1,my2,mx2)
print(chess([[0,0,0,0],[1,9,9,9],[0,0,0,0],[1,9,9,9]]))
# Funkcja rekurencyjnie odcina n-1 elementów liczby n-elementowej tak aby usyskac wszystkie kombinacje
# Jeżeli liczba elementów w przekazywanej tablicy jest pierwsza i każdy jej element też to zwracana jest wartośc true