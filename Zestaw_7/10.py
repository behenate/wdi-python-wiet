"""
    Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
    funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
    powstać nowa lista.
"""


class Digit:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


n1 = Digit(7, Digit(9, Digit(7)))
n2 = Digit(1, Digit(6, Digit(5)))

