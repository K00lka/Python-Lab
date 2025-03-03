def odliczanie(n,x):
    for i in range(n, -1, -1):
        if i % x == 0:
            continue
        print(i, end=', ')
    print('Koniec')

odliczanie(10, 3)


