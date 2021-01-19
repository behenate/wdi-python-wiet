"""
    6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
    funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
    wartość.
"""


class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


a = Node(10)


def insert_end(first, elem):
    if first is None:
        return elem
    previous = first
    while previous.next is not None:
        previous = previous.next
    previous.next = elem
    return first
