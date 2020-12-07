
# x, y aktualny wiersz
# tab - tablica
#s - sume
#k1,k2 2 poprzedni królowie
def kings(x,y, tab, s, k1, k2 ):
    N = len(tab)
    if y==N:
        print(s)
        if s == 0:
            print("Da sie")
            return True
        else:
            print("Nie da sie")
    else:
        for n in range(N):
            if (abs(n - k1[0]) >= 2 or abs(y - k1[1]) >= 2) and (abs(n - k2[0]) >= 2 or abs(y - k2[1]) >= 2):
                kings(n, y+1, tab, s+tab[y][n], k1=k2, k2=[n, y])

    # if (abs(x-k1[0]) >= 3 or abs(y-k1[1]) >= 3) and (abs(x-k2[0]) >= 3 or abs(y-k2[1]) >= 3):
    #     kings(0, y+1, tab, s+tab[y][x], k1=k2, k2=[x, y])



tab = [
    [ 1,  0,  0,  0,  0,  0,  0],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5],
    [-5, -5, -5, -5, -5, -5, -5],
    [ 5,  5,  5,  5,  5,  5,  5]
]
for n in range(len(tab)):
    print(kings(n, 0, tab, 0, [-3, -3], [-3, -3]))