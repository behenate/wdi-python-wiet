"""
Zadanie 2.
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
"""
primes = {2, 3, 5, 7}
arr = [0] * 9
arr[0] = 1

cnt = 0
def recur_place(T, num=0, index=0):
    if ((num in primes and arr[index - 1] in primes) or abs(arr[index - 1] - num) < 2) and index != 0:
        return False
    arr[index] = num
    if index == 8:
        global cnt
        cnt += 1
        print(arr)

    for i in range(1, 10):
        place = True
        for elem in arr:
            if elem == i:
                place = False
                break
        if place:
            if recur_place(T, i, index + 1):
                return True
    arr[index] = 0
    return False


recur_place(arr, arr[0], 0)
print(cnt)