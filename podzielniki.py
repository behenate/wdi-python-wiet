def reverse_list(list):
    n = len(list)
    for i in range(0, (n//2)):
        list[i], list[n-i-1] = list[n-i-1], list[i]

l = [2,3,4,6,7]
print(reverse_list(l))
print(l)