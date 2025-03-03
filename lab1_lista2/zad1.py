def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

assert silnia(2) == 2
assert silnia(3) == 6
assert silnia(4) == 24