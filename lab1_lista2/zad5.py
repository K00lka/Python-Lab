def name_content(name_list, a):
    i = 0
    for name in name_list:
        if a in name:
            i += 1
        
    
assert name_content(['Darek', 'Ala', 'Renatka'], 'a') == 2
print('Test passed')
assert name_content(['Marek', 'Ada', 'Renatka', 'Dawid'], 'a') == 3
print('Test passed')
assert name_content(['Renatka', 'Darek'], 'a') == 3
print('Test passed')