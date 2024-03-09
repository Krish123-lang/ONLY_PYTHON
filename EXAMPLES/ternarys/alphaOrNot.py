char = input("Enter a character: ")

isAlphabet = True if char.isalpha() else False
print("Alphabet" if isAlphabet else "Not alphabet")

'''
Enter a character: 4
Not alphabet

------------------------

Enter a character: e
Alphabet
'''