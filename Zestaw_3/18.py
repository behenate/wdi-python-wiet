"""
Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

"""


def znajdz_palindrom(t):
    l_t = len(t)
    max_len = 0
    for p in range(l_t):
        if t[p] % 2 == 1:
            for k in range(l_t-1, p-1, -1):
                cp = p
                ck = k
                while cp < ck:
                    if t[cp] != t[ck] or t[cp] % 2 == 0:
                        break
                    cp += 1
                    ck -= 1
                if not (cp < ck):
                    max_len = max(max_len, k-p+1)
    return max_len


t1 = [1, 3, 3, 1]
print(znajdz_palindrom(t1))



