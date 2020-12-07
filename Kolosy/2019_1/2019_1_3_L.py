from random import randint
def rekurencja_3(tablica,suma,row,krol_pierwszy,krol_drugi,N):
    if row == N and suma == 0:
        print("Można")
        return True
    elif row == N:
        return False
    for i in range(N):
        roznica = krol_pierwszy - i
        if roznica < 0:
            roznica *= -1
        if roznica <= 2:
            continue
        roznica = krol_drugi - i
        if roznica < 0:
            roznica *= -1
        if roznica <= 2:
            continue
        suma = suma + tablica[row][i]
        return rekurencja_3(tablica,suma,row+1,krol_drugi,i,N)
    return False
N = 7
tablica = [
    [ 1,  0,  0,  0,  0,  0,  0],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5]
]
print(rekurencja_3(tablica,0,0,-5,-5,N))