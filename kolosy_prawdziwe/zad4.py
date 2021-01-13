#Wojciech Dróżdż
# Funkcja rekurencyjnie odcina n-1 elementów liczby n-elementowej tak aby usyskac wszystkie kombinacje
# Jeżeli liczba elementów w przekazywanej tablicy jest pierwsza i każdy jej element też to zwracana jest wartośc true

def num_len(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

def is_prime(m):
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int((m ** (1 / 2))) + 1, 2):
        if m % i == 0:
            return False
    return True

def divide(N):
    start_len = num_len(N)

    def recur_divide(n, start_len, div_tab=None, iteration = 0):
        if div_tab is None:
            div_tab = []
        if iteration == start_len:
            n_t = [n] + div_tab
            print(n_t)
            all_primes = True
            num_elems = len(n_t)
            all_primes = is_prime(num_elems)
            for elem in n_t:
                if not is_prime(elem):
                    all_primes = False
            if all_primes:
                return True
            return False
        n_len = num_len(n)
        for i in range(n_len):
            n_next = n // (10**i)
            n_to_tab = n % (10**i)
            n_tab =[n_to_tab] + div_tab if n_to_tab != 0 else div_tab
            if recur_divide(n_next, start_len, n_tab, iteration+1):
                return True
        return False
    return recur_divide(N, start_len)

print(divide(65465489))
