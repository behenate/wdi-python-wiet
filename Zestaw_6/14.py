"""
Zadanie 14. Problem wież w Hanoi (treść oczywista)
"""
A = [1, 2, 3, 4]
B = [0]*len(A)
C = [0]*len(A)


def hanoi(n, A, B, C, i=0):
    if n > 0:
        hanoi(n-1, A, C, B, i+1)
        C[i] = A[i]
        A[i] = 0
        hanoi(n-1, B, A, C, i+1)


hanoi(4, A, B, C)
print(C)