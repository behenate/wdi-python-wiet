def get_lenght():
    global number

    print(number)
    lenght = 0

    while number != 0:
        number = number // 10
        lenght += 1

    return lenght


def give_number():
    global number

    print(number)

    var = number % 10
    number = number // 10

    return (var)


number = int(input("Podaj liczbę: "))
lenght = get_lenght()
lastNumber = give_number()
print(lastNumber)
print(lenght)