
# Funkcja konwertująca
def convert_to(num, system):
    n = num
    length = 0
    # W systemach 11-16 pojawiają się litery, kiedy reszta jest > 9. Tu jest słownik do nich
    dictionary = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    # Sprawdź długość liczby co wyjdzie
    while n > 0:
        n //= system
        length += 1
    result = [0]*length

    # Konwersja na system i wpisanie w odpowiednie pole tablicy
    for i in range(length):
        to_append = num % system
        if to_append > 9:
            to_append = dictionary[to_append]
        result[length - i - 1] = to_append
        num //= system
    # Zamiana tablicy na string
    result_str = ""
    for elem in result:
        result_str += str(elem)
    return result_str


print(convert_to(256,16))