from random import randint

def czyjestkwadratem(n,a): #czy liczba n jest co najmniej drugą potęgą liczby a
    while(n>1):
        if(n%a != 0):
            return False
        n=n//a
    return True

N = 1000
t1 = [randint(0,1) for i in range(N)]
t2 = [randint(0,1) for i in range(N)]
# t1 = [1,0,0,1,1,0,1,1,1,0,0,0]
# t2 = [0,0,0,0,0,0,1,1,1,0,0,0]
N = len(t1)
a = 3 #liczba
print(t1)
print(t2)

#sumy prefiksowe
sumpref1 = [0]*(N+1)
sumpref2 = [0]*(N+1)

for i in range(1,N+1):
    sumpref1[i] = sumpref1[i-1]+t1[i-1]
    sumpref2[i] = sumpref2[i-1]+t2[i-1]

czymozna=False
dlug1 = 1
while(dlug1<24 and dlug1<=N):
    dlug2 = 24-dlug1
    x=0
    while(x+dlug1-1<N):
        y=0
        while(y+dlug2-1<N):
            if(czyjestkwadratem(sumpref1[x+dlug1]-sumpref1[x]+sumpref2[y+dlug2]-sumpref2[y],a)):
                czymozna=True
            y+=1
        x+=1
    dlug1+=1

print(czymozna)