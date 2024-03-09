def Palindrome(word):
    return word == word[::-1]


word = input("Enter something: ")
ans = Palindrome(word)

if ans:
    print(f"{word} is Palindrome")

else:
    print(f"{word} is Not Palindrome")


'''
Enter something: 121
121 is Palindrome

--------------------------

Enter something: apple
apple is Not Palindrome
'''
