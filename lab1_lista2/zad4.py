def name_lenght(name_list):
    return [len(name) for name in name_list]

assert name_lenght(['Darek', 'Ala', 'Renatka']) == [5, 3, 7]
print('Test passed')
assert name_lenght(['Marek', 'Ada', 'Renatka', 'Dawid']) == [5, 3, 7, 5]
print('Test passed')
assert name_lenght(['Renatka', 'Darek']) == [7,5]
print('Test passed')