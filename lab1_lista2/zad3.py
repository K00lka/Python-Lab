def palindrome (s):

    if s == s[::-1]:
        return True
    else:
        return False

if palindrome("kajak") == True:
    print ('Tak')
else:
    print ('Nie')

