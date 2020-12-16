"""

1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru

"""


class Node:
    def __init__(self, value, prev=None, nex=None):  # last, next
        self.value = value
        self.prev = prev
        self.nex = nex


class Set:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        if self.first is None:
            self.first = self.last = Node(value)
            return
        node = self.first
        while node is not None and node.value <= value:
            if node.value == value:
                return
            node = node.nex
        if node == self.first:
            self.first.prev = self.first = Node(value, None, self.first)
            return
        if node is None:
            self.last.nex = self.last = Node(value, self.last)
            return
        new_node = Node(value, node.prev, node)
        node.prev.nex = new_node
        node.prev = new_node

    def remove(self, value):
        node = self.first
        while node is not None and node.value < value:
            node = node.nex
        if node == self.first:
            self.first = self.first.nex
            self.first.prev = None
            return
        if node == self.last:
            self.last = self.last.prev
            self.last.nex = None
            return
        node.prev.nex = node.nex
        node.nex.prev = node.prev

    def print_vals(self):
        node = self.first
        while node is not None:
            print(node.value)
            node = node.nex

    def is_in_set(self, val):
        node = self.first
        while node is not None and node.value <= val:
            if node.value == val:
                return True
            node = node.nex
        return False


set = Set()
set.add(10)
set.add(12)
set.add(13)
set.add(14)
set.add(9)
set.add(8)
set.print_vals()
print(set.is_in_set(9))
set.print_vals()