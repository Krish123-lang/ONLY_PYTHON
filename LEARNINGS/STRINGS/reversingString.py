# Simple way

#a="Hello krishna"
#l1=[1,2,3,4,5]

# print(a[::-1]) # anhsirk olleH
#print(l1[::-1]) #  reverses a list: [5, 4, 3, 2, 1]

# ***************************************************************************
# Using Loops
'''
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
'''

'''
The original string is : Geeksforgeeks
The reversed string(using loops) is : skeegrofskeeG
'''
# ***************************************************************************
# Using recursion
'''
def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]


s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))
'''

'''
The original string is : Geeksforgeeks
The reversed string(using recursion) is : skeegrofskeeG
'''
# ***************************************************************************

# Function to reverse a string
'''
def reverse(string):
    string = string[::-1]
    return string
 
s = "Geeksforgeeks"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))
'''

'''
The original string is : Geeksforgeeks
The reversed string(using extended slice syntax) is : skeegrofskeeG
'''

# Deleting an entire string
'''
a="Hello world"
del a
print("A Deleted successfully")
'''