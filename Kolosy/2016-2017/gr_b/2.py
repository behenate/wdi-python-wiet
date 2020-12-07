import random
t = [random.randint(100, 999) for _ in range(100)]
N = len(t)
def find(tab, N):
    for sub_len in range(N-1, -1, -1):
        sub = [0]*sub_len
        for offset in range(N-sub_len+1):
            for i in range(offset, offset+sub_len):
                sub[i-offset] = tab[i]
            for s_offset in range(N-sub_len+1):
                found = True
                for i in range(s_offset, s_offset+sub_len):
                    if tab[i] != sub[s_offset+sub_len-1-i]:
                        found = False
                        break
                if found:
                    return len(sub)
    return 1
print(find(t, N))
