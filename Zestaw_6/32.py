import time
start = time.time()
target_k = 2
tab = [1,5, 11, 5]
def subset (T, k_x, k_y, s_x, s_y, i):
    print("")
    print(k_x, k_y)
    print(s_x,s_y)

    if k_x == target_k and k_y == target_k and s_x == s_y:
        return True
    if k_x > target_k or k_y > target_k or i >= len(T):
        return False
    return subset(T, k_x + 1, k_y, s_x+T[i], s_y, i+1) or subset(T, k_x, k_y+1 , s_x, s_y+T[i], i+1) or subset(T, k_x, k_y, s_x, s_y, i+1)

print(subset(tab, 0, 0, 0, 0, False))

print(time.time()-start)