"""
Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe
"""

def prime_factors(T):
    print(T)
    factors_tab = [None]*len(T)
    for i, elem in enumerate(T):
        factors = set()
        j=2
        if elem == 1:
            continue
        while elem > 1:
            if elem % j == 0:
                factors.add(j)
            while elem % j == 0:
                elem //= j
            j += 1
        factors_tab[i] = factors
    return factors_tab


def jump(index, jump_cnt=0):
    if index == len(T)-1:
        return jump_cnt
    if index >= len(T):
        return False
    jumps = factors_T[index]
    if len(jumps) == 0:
        return False
    for move in jumps:
        j_c = jump(index+move, jump_cnt+1)
        if j_c > 0:
            return j_c
    return -1

T = [243, 81, 70, 9, 7,7,7]
factors_T = prime_factors(T)
print(jump(0))