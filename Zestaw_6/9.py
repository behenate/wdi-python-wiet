"""
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej
masy. Odważniki można umieszczać tylko na jednej szalce.
"""


def measure_mass(weights, target_mass, mass=0, iterations=0, used_weights=[]):
    if len(used_weights) == 0:
        used_weights = [0]*len(weights)
    if mass == target_mass:
        print("Used weights: ", end="")
        for elem in used_weights:
            if elem !=0:
                print(elem,end=", ")
        print()
        return True
    if mass > target_mass or iterations >= len(weights):
        return False
    a = used_weights[:]
    a[iterations] = weights[iterations]
    return measure_mass(weights, target_mass, mass + weights[iterations], iterations + 1, a) \
        or measure_mass(weights, target_mass, mass, iterations + 1) \
        or measure_mass(weights, target_mass + weights[iterations], mass, iterations + 1, a)


T = [2,2,2,2,5]
print(measure_mass(T, 3))
