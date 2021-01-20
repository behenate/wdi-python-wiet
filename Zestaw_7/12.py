"""
    Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
    jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
    leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
    dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
    oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
    czy w wyniku operacji moc zbioru uległa zmianie.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.ord = ord(value)


class NM:
    def __init__(self, cnt=0):
        self.cnt = cnt


def add_letter(first, letter, nm):
    elem = first
    letter = Node(letter)
    while elem is not None:
        if elem.ord == letter.ord:
            break
        if elem.next is None:
            elem.next = letter
            nm.cnt += 1
            break

        if elem.ord < letter.ord < elem.next.ord:
            letter.next = elem.next
            elem.next = letter
            nm.cnt += 1
            break
        elem = elem.next


def add_word(word, first, nm):
    p = nm.cnt
    for letter in word:
        add_letter(first, letter, nm)
    return nm.cnt > p

nm = NM()
c = Node("c")
b = Node("b", c)
a = Node("a", b)

print(add_word("qwertyuiopasdfghjklzxcvbnm", a, nm))

