import time
start = time.time()
t1 = [i for i in range(10000)]
t2 = [i+3 for i in(range(10000))]

do_usun = []
s2=0
for i in range(len(t1)):
    e1 = t1[i]
    for j in range(s2, len(t2)):
        e2 = t2[j]
        if e1 == e2:
            do_usun = do_usun + [e1]
            s_2 = j+1
        elif e2 > e1:
            break
print(do_usun)
print(time.time()-start)