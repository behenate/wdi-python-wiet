"""
    Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
    należy przekazać wskazanie na pierwszy element listy.
"""


class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


d = Node(40)
c = Node(30, d)
b = Node(20, c)
a = Node(10, b)

def remove_last(first):
    if first.next is None:
        return None
    next = first.next
    std = first
    while next.next is not None:
        next = next.next
        std = std.next
    std.next = None
    return std

res = remove_last(a)