"""
2. Zastosowanie listy odsyłaczowej do implementacji
tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.

"""

class Elem:
    def __init__(self, value, index, prev_e=None, next_e=None):
        self.value = value
        self.index = index
        self.prev_e = prev_e
        self.next_e = next_e


class SparseArr:
    def __init__(self):
        self.first_e = None
        self.last_e = None

    def set_index(self, index, value):
        elem = Elem(value, index)
        if self.first_e is None:
            self.first_e = self.last_e = elem
            return
        if index > self.last_e.index:
            self.last_e.next_e = elem
            elem.prev_e = self.last_e
            self.last_e = elem
        elif index < self.first_e.index:
            elem.next_e = self.first_e
            self.first_e.prev_e = elem
            self.first_e = elem
            return
        existing_elem = self.first_e
        while existing_elem.index <= index:
            if existing_elem.index == index:
                existing_elem.value = value
                return
            existing_elem = existing_elem.next_e

        existing_elem.prev_e.next_e = elem
        existing_elem.prev_e = elem
        elem.prev_e = existing_elem.prev_e
        elem.next_e = existing_elem.next_e

    def get_index_val(self, index):
        e = self.first_e
        while e.index <= index:
            if e.index == index:
                return e.value
            e = e.next_e
        return None


sparse_arr = SparseArr()
sparse_arr.set_index(0, 11)
sparse_arr.set_index(1, 40)
sparse_arr.set_index(1, 345)
sparse_arr.set_index(2, 40)
sparse_arr.set_index(3, 30)
sparse_arr.set_index(0, 10)
for i in range(0,4):
    print(sparse_arr.get_index_val(i))