def generuj_spirale(n):
    n = n if n%2==1 else n+1

    tab = [[0 for _ in range(n)] for _ in range(n)]

    i = n//2
    j = n//2
    m_moves = 1 #  Ilość ruchów do wykonania.
    moves = [1, 0, 0, 0]  #  Wygodny sposób przechowywania ruchu bez miliona ifów
    m_cnt = 1  #  Pozostała ilość ruchów do wykonania. M_moves ją nadpisuje jak się skończy
    dir = 0  #  Kierunek w którym się rusza. Czyli po prostu index moves do którego sie doda m_moves
    add = True  #  Czy dodawać do ilości ruchów co można wykonać. Powinno dodawać co 2 zmianę kierunku
    for l in range(n**2):
        tab[i][j] = l + 1
        j += moves[0] - moves[2]
        i += moves[3] - moves[1]

        m_cnt -= 1
        # Jak skończyła się ilość ruchów zmień kierunek
        if m_cnt == 0:
            add = not add
            if add:
                m_moves += 1
            m_cnt = m_moves
            dir = (dir+1) % 4
            moves = [0, 0, 0, 0]
            moves[dir] = 1

    return tab

def printuj_spirale(spirala):
    for line in spirala:
        for elem in line:
            print(str(elem).rjust(5), end="")
        print("")