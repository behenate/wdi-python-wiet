def subset(index=0, index_sum=0, value_sum=0):
    if index_sum == value_sum and index_sum !=0:
        return index_sum
    if index + 1 > len(tab) or index_sum > 10:
        return False

    r2 = subset(index + 1, index_sum + index, value_sum + tab[index])
    r1 = subset(index + 1, index_sum, value_sum)
    if type(r1) is int:
        return r1
    elif type(r2) is int:
        return r2
    else:
        return False


tab = [2323, 12, 3, 1, 5, 112, 11, 27]
print(subset())
