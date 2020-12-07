t1 = [1, 2, 3,  4,  5,  6,  7,  8]
t2 = [5, 6, 7,  8,  9, 10, 11, 12]
t3 = [6, 7, 8, 11, 13, 15, 16, 18]
t = [t1, t2, t3]

ind_tab = [0, 0, 0]
lens = [len(t1), len(t2), len(t3)]

smol = min(t1[0], t2[0], t3[0])

master_counter = 0
top = max(t1[lens[0]-1], t2[lens[0]-1], t3[lens[0]-1]) +1
while smol != top:
    counter = 0
    for i in range(3):
        while ind_tab[i] < lens[i] and t[i][ind_tab[i]] < smol:
            ind_tab[i] += 1
        if ind_tab[i] < lens[i] and t[i][ind_tab[i]] == smol:
            ind_tab[i] += 1
            counter += 1
    master_counter += counter // 3
    c = 0
    smol = top
    for i in range(3):
        if ind_tab[i] < lens[i]:
            c += 1
            smol = min(t[i][ind_tab[i]], smol)
print(master_counter)