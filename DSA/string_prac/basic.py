str1 = 'krishna is awesome'
# print(str1[0])

# for i in str1:
#     print(i)

str2 = 'are you sure?'
# print(str1 + " " + str2)

# print(str1[::-1]) # reversing a string
'''
str_input = input("Enter a string: ")
if str_input == str_input[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
'''
'''
Enter a string: racecar
The string is palindrome
'''

# print(str1)
# del str1
# print(str1)

'''
print(str1)
s1 = "Bob"+str1[1:]
print(s1) # Bobrishna is awesome
'''

s = str1.replace('krishna', 'bob')
# print(s) # bob is awesome

# print(len(str1)) # 18
print(str1.upper())  # KRISHNA IS AWESOME
print(str1.lower())  # krishna is awesome
print(str1.encode())  # b'krishna is awesome'
print(str1.capitalize())  # Krishna is awesome
print(str1.isalnum())  # False
print(str1.title())  # Krishna Is Awesome
print(str1.index('w'))  # 12
print(str1.find('e'))  # 13
print(str1.endswith('r'))  # False
print(str1.count('e'))  # 2

strip_text = "      krishna              "
print(strip_text.strip())  # krishna
print(strip_text * 3)

print('is' in str1) # True
print('is' not in str1) # False
