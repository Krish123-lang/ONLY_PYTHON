'''
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

Syntax: string.find(value, start, end)
'''

'''
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x) #7
'''

# ***************************************************************

txt = "Hello, welcome to my world."

x = txt.find("e")

# print(x) # 1

x = txt.find("e", 5, 10)

# print(x) # 8

# If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(txt.find("q")) # -1
print(txt.index("q")) # substring not found