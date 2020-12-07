def czypierwsza(n):
    if(n<2):
        return False
    if(n==2 or n==3):
        return True
    k=2
    while(k*k<=n):
        if(n%k==0):
            return False
        k+=1
    return True

def sprawdz(i):
    if(i==n):
        return True
    liczba = 0
    for j in range(i,n):
        liczba=liczba*2 + tab[j]
        if(czypierwsza(liczba) and sprawdz(j+1)):
            return True
    return False

tab = [1,1,0,1,0,0]
n=len(tab)
print(sprawdz(0))