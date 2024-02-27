'''
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.

Syntax: string.index(value, start, end)
'''

txt = "Hello, welcome to my world."
'''

x = txt.index("to")

print(x) # 15
'''
# ****************************************************************


# x = txt.index("e")

# print(x) # 1

# ******************************************************************

# x = txt.index("e", 5, 10)

# print(x) # 8
# ******************************************************************


print(txt.find("q"))  # -1
print(txt.index("q")) # ValueError: substring not found
