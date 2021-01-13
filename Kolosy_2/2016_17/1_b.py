"""
Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
znalezionych i wypisanych sum.
"""
def is_prime(m):
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int((m ** (1 / 2))) + 1, 2):
        if m % i == 0:
            return False
    return True

N = 4
t1 = [1,3,2,4]
t2 = [9,7,4,8]

def recur_sum(s=0, index=0, path = []):
    if index == N:
        if is_prime(s):
            print(path, s)
        return

    recur_sum(s + t1[index], index+1, path+[t1[index]])
    recur_sum(s + t2[index], index+1, path+[t2[index]])
    recur_sum(s + t2[index] + t1[index], index + 1, path + [t2[index], t1[index]])
recur_sum()