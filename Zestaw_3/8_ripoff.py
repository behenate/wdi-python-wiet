def czy_pierwsza(n):
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    k = 2
    while(k*k<=n):
        if(n%k==0):
            return False
        k+=1
    return True

ta = [20, 150, 2, 200, 300, 195, 14, 15, 3, 3, 18, 21, 300, 3, 6, 3, 5, 12, 1]
z = len(ta)


tb = [False]*z #tablica przechowuje informacje czy mozna na to pole wskoczyć z pierwszego pola
tb[0] = True

for i in range(z):
    if(tb[i]==True):
        k=2
        num = ta[i] #przypisuje liczbe z pola o indeksie i
        while(k<=num and k<z-i):
            if(num%k==0):
                if(czy_pierwsza(k)):
                    tb[i+k]=True
            k=k+1

print(tb)