"""
3. Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.
"""

t1 = [1, 2, 3,  4,  5,  6,  7,  8]
t2 = [5, 6, 7,  8,  9, 10, 11, 12]
t3 = [6, 7, 8, 11, 13, 15, 16, 18]

t = [t1, t2, t3]
c_m = min(t1[0], t2[0], t3[0])
ci = [0, 0, 0]
lens = [len(t1)-1, len(t2)-1, len(t3)-1]
MAX = 1000000000000000000000000000000000
reps = {}
master_cnt = 0

while c_m < MAX:
    counter = 0
    for i in range(3):
        while ci[i] < lens[i] and t[i][ci[i]] < c_m:
            ci[i] += 1
        if ci[i] < lens[i] and t[i][ci[i]] == c_m:
            counter += 1
            ci[i] += 1


    if counter == 3:
        master_cnt += 1
    c_m = MAX
    for i in range(3):
        if ci[i] < lens[i]:
            c_m = min(t[i][ci[i]], c_m)
    # if c_m > MAX:
    #     print(c_m)
    #     break
print(master_cnt)