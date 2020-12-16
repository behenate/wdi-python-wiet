"""
Zadanie 27. Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają
proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku
"""


def col(square1, square2):
    ax1, ax2, ay1, ay2 = square1
    bx1, bx2, by1, by2 = square2
    if bx2 < ax1 or bx1 > ax2 or ay1 > by2 or ay2 < by1 or (bx2 < ax2 and bx1 > ax1 and by1 > ay1 and by2 < ay2):
        return False
    # ax1, ax2, ay1, ay2 = square2
    # bx1, bx2, by1, by2 = square1
    # if bx2 < ax1 or bx1 > ax2 or ay1 > by2 or ay2 < by1 or (bx2 < ax2 and bx1 > ax1 and by1 > ay1 and by2 < ay2):
    #     return False
    return True


def check_for_col(squares_list):
    for i in range(len(squares_list) - 1):
        if col(squares_list[i], squares_list[len(squares_list) - 1]):
            return True
    return False


def area(square):
    x1, x2, y1, y2 = square
    return (x2 - x1) * (y2 - y1)


def squares_combinations(all_squares, used_squares_list=list(), total_area=0, last_index=0):
    if check_for_col(used_squares_list) or total_area > 2012:
        return False
    if len(used_squares_list) == 13:
        print("Found 13 Squares! Total area is:", total_area)
        if total_area == 1012:
            print("Found 1012 Square!!!!")
            return True
        return False
    for i in range(last_index, len(all_squares)):
        sq = all_squares[i]
        if squares_combinations(all_squares, used_squares_list + [sq], total_area + area(sq), i):
            return True
    return False


tab = [
    (20, 40, 0, 10),
    (10, 20, 10, 20),
    (1000, 1002, 1000, 1002),
    (1003, 1005, 1003, 1005),
    (1006, 1008, 1006, 1008),
    (55, 65, 55, 65),
    (66, 76, 66, 76),
    (77, 87, 77, 87),
    (88, 98, 88, 98),
    (0, 10, 0, 10),
    (11, 21, 11, 21),
    (22, 32, 22, 32),
    (33, 43, 33, 43),
    (44, 54, 44, 54),
    (120, 130, 120, 130),

]
print(squares_combinations(tab))
