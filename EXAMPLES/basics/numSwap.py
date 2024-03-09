num1 = 4
num2 = 8

print(f"Before swapping: {num1},{num2}")

# Using third variable
'''
temp = num1
num1 = num2
num2 = temp
'''

# With out using third variable
'''
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
'''

# easy way in python
num1, num2 = num2, num1

print(f"After swapping: {num1},{num2}")

'''
Before swapping: 4,8
After swapping: 8,4
'''
