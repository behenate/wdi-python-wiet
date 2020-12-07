
# Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

max_iterations = 0
max_index = 0
for i in range(2, 10000):
    a = i
    iterations = 0
    while a != 1:
        iterations += 1
        an = a % 2 * (3 * a + 1) + (1 - a % 2) * a/2
        a = an
    if iterations > max_iterations:
        max_iterations = iterations
        max_index = i

print("Maksymalna liczba iteracji ({}) dla liczby {}".format(max_iterations, max_index))
