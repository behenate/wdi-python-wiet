tab = [1, 3, 5, 3, 2]
N = len(tab)

max_ln = 0
for start in range(N//2):
    for end in range(N-1, start, -1):
        ln = 0
        for i in range((end-start//2)-1):
            _i = start + i
            j = end-i
            print(i, j)
            if tab[_i] == tab[j] and tab[_i]%2 == 1:
                if _i == j:
                    ln += 1
                else:
                    ln += 2
            else:
                ln = 0
                break
        if ln > max_ln:
            max_ln = ln
            print(start, end, ln)