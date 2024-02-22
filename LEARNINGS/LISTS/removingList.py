l1=[1,2,3,4,"ohio",5]
# using pop() function
'''
#l1.pop() # [1, 2, 3, 4]
l1.pop(3) # [1, 2, 3, 5] => removes the 3rd position of element i.e. 4
print(l1)
'''

# Using remove() function => removes the given element
'''
#l1.remove(3) # [1, 2, 4, 5]
#l1.remove(2) # [1, 3, 4, 5]
#l1.remove("ohio") # [1, 2, 3, 4, 5]
print(l1)
'''

#using del keyword
'''
# del l1[0] # [2, 3, 4, 'ohio', 5] => removing first element
del l1 # deletes entire list including the l1 variable
print(l1)
'''

# using clear function to empty a list
'''
l1.clear() # []
print(l1)
'''