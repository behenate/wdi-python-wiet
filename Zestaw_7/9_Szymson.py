class Node:
    def __init__(self, value=0, prev_e=None, next_e=None):
        self.value = value
        self.prev = prev_e
        self.next = next_e
e1 = Node(9)
e2 = Node(9, e1)
e1.next_e = e2
e3 = Node(8, e2)
e2.next_e=e3

def increase_by_one(first):
    first = Node()
    p = first.next
    q = first.prev
    while p is not None:
        q = first
        first = p
        p = first.next
    if p is None:
        q = first
        first = p
        p = None
    if first.value != 9:
        first.value += 1
    else:
        while first.value == 0:
            first.value += 1
            first = q
            q = first.prev
        q.value += 1
increase_by_one(e1)