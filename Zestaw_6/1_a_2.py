def rekur(l,n=0, c=0):
    _l = n
    cnt = 0

    while _l > 0:
        _l//=10
        cnt+=1

    if l == 0:
        if cnt > 1:
            print(n)
        return
    # print(l, n, ((l%10)*(10**c)))

    rekur(l//10, (10**c)*(l % 10)+n, c+1)
    rekur(l//10, n, c)

liczba = 1234
rekur(liczba)

