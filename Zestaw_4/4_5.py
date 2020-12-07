"""

Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa.

"""
tab = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
x = len(tab[0])
y = len(tab)

sum_rows = [0]*y
sum_cols = [0]*x
for i, row in enumerate(tab):
    sum = 0
    for elem in row:
        sum += elem
    sum_rows[i] = sum

for j in range(x):
    sum = 0
    for k in range(y):
        sum += tab[k][j]
    sum_cols[j] = sum


max = 0
max_m = 0
max_n = 0
for m in range(x):
    for n in range(y):
        div = sum_cols[m] / sum_rows[n]
        if div > max:
            max = div
            max_m = m
            max_n = n

print(sum_rows)
print(sum_cols)
print(max, max_m, max_n)

