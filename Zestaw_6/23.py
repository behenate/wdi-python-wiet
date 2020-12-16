"""
Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.
"""
from copy import deepcopy
T = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130]

def calculate_resistance(resistor_tab):
    to_serial_tab = [0]*len(resistor_tab)
    for i, parallels in enumerate(resistor_tab):
        add = 0
        for j in range(0, len(parallels)):
            if parallels[j] == 0:
                continue
            add += 1/parallels[j]
        if add == 0:
            to_serial_tab[i] = 0
            continue
        to_serial_tab[i] = 1/add
    resistance = 0
    for elem in to_serial_tab:
        resistance += elem
    return resistance


def find_resistance(resistors_left, target, resistor_list=None, iteration=0):
    if resistor_list is None:
        resistor_list = [[0 for _ in range(3)] for _ in range(3)]
    if calculate_resistance(resistor_list) == target:
        print(resistor_list)
        return True
    if len(resistors_left) == 0 or iteration == 3:
        return False
    for i, resistor in enumerate(resistors_left):
        r_l_pass = [[] for _ in range(len(resistors_left) - 1)]
        c = 0
        for j in range(len(resistors_left)):
            if j == i:
                continue
            r_l_pass[c] = resistors_left[j]
            c += 1
        found = False
        found = found or find_resistance(r_l_pass, target, resistor_list, iteration + 1)
        for k in range(3):
            res_list_pass = deepcopy(resistor_list)

            res_list_pass[k][iteration] = resistor
            found = found or find_resistance(r_l_pass, target, res_list_pass, iteration + 1)
            if found:
                return True
    return found


print(find_resistance(T, 25))