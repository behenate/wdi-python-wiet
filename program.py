sigmy = [
    [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3],
    [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1],
    [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
]


def zlozenie(arr_1, arr_2):
    res_arr = [0]*len(arr_1)
    for i in range(len(arr_1)):
        res_arr[i] = arr_1[arr_2[i]-1]
    return res_arr


def find_in_arr(arr):
    for i, elem in enumerate(sigmy):
        if arr == elem:
            return i


for y in sigmy:
    print("", end="")
    for x in sigmy:
        print("σ" + str(find_in_arr(zlozenie(y, x))+1), end=" ")
    print("")