"""
Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym
wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

arr = []
while True:
    num = float(input("Give me the value"))
    add_arr = [num]
    added = False
    if num==0:
        break
    for i, elem in enumerate(arr[:10]):
        if num >= elem:
            new_arr = arr[:i] + add_arr + arr[i:]
            added = True
            break
    if not added:
        new_arr = arr + add_arr
    arr = new_arr
print(arr)
