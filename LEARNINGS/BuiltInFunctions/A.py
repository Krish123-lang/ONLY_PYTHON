# ABS => Returns the absolute value of a number => Returns True if all items in an iterable object are true => Returns True if any item in an iterable object is true

# print(abs(-3)) # 3
# ************************************************************************************

# ALL => Returns True if all items in an iterable object are true => Returns True if any item in an iterable object is true
'''
The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
'''

'''
mylist = [True, False, True]
mylist = [0, 1, 2, 3]
print(all(mylist))  # False

mydict = {0: "True", 1: "False"}
print(all(mydict)) # False
'''
# ************************************************************************************

# ANY => Returns True if any item in an iterable object is true
'''
mylist = [0, 1, False]
x = any(mylist)
print(x) # True
'''
# ************************************************************************************

