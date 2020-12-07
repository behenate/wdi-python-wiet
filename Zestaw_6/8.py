"""
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej
masy. Odważniki można umieszczać tylko na jednej szalce.
"""


def measure_mass(weights, target_mass, mass=0, iterations=0):
    if mass == target_mass:
        return True
    if mass > target_mass or iterations >= len(weights):
        return False
    return measure_mass(weights, target_mass, mass + weights[iterations], iterations + 1) \
        or measure_mass(weights, target_mass, mass, iterations + 1) \
        or measure_mass(weights, target_mass + weights[iterations], mass, iterations + 1)


T = [2,3,1]
print(measure_mass(T, 4))
