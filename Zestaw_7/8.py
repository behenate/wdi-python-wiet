"""
    8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
    element listy. Do funkcji należy przekazać wskazanie na pierwszy element
    listy.
"""
class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

g = Node(70)
f = Node(60, g)
e = Node(50, f)
d = Node(40, e)
c = Node(30, d)
b = Node(20, c)
a = Node(10, b)

def remove_every_other(first):
    if first.next is None:
        return first
    curr = first
    while curr.next is not None and curr.next.next is not None:
        curr.next = curr.next.next
        curr = curr.next
    if curr.next is not None:
        curr.next = None
    return first

ret = remove_every_other(a)
print(ret)
while ret is not None:
    print(ret.value)
    ret = ret.next