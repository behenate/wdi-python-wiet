"""
Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.

W spirali to jest moje zdrowie psychiczne na tym gównianym kierunku
"""

n = 5
n = n if n%2==1 else n+1

tab = [[0 for _ in range(n)] for _ in range(n)]

i = n//2
j = n//2
m_moves = 1
moves = [1, 0, 0, 0]
m_cnt = 1
dir = 0
add = True

for l in range(n**2):
    tab[i][j] = (n*n) - l
    j += moves[2] - moves[0]
    i += moves[1] - moves[3]

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


for line in tab:
    for elem in line:
        print(str(elem).rjust(5), end="")
    print("")

