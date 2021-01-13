class Elem:
    def __init__(self, value, prev_e=None, next_e=None):
        self.value = value
        self.prev_e = prev_e
        self.next_e = next_e

e1 = Elem(9)
e2 = Elem(7, e1)
e1.next_e = e2
e3 = Elem(9, e2)
e2.next_e=e3
def add1(e1):
    e = e1
    while e.next_e is not None:
        e = e.next_e
    e.value += 1

    while e.value > 9:
        e.value -= 1
        if e.prev_e is not None:
            e = e.prev_e
        else:
            e.prev_e = Elem(0, None, e)
            e = e.prev_e
            e1 = e
        e.value = e.value+1
    e=e1
    while e.next_e is not None:
        print(e.value)
        e = e.next_e
    print(e.value)
add1(e1)