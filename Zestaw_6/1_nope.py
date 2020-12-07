def czypierwsza(n):
    if(n<2):
        return False
    if(n==2 or n==3):
        return True
    k = 2
    while(k*k<=n):
        if(n%k==0):
            return False
        k+=1
    return True


def usun(liczba,liczba_cyfr,nr_cyfry,zbior):
    if(liczba_cyfr == 1):
        return True
    else:
        liczba = (liczba-liczba%(10**nr_cyfry))//10 + liczba%(10**(nr_cyfry-1))
        if(czypierwsza(liczba)):
            zbior.add(liczba)
        for i in range(1,liczba_cyfr+1):
            usun(liczba,liczba_cyfr-1,i,zbior)

liczba = 12345
liczba_cyfr = 5
zbior = set()
for i in range(1,liczba_cyfr):
    usun(liczba,liczba_cyfr-1,i,zbior)
print(zbior)