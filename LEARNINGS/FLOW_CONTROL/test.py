def AreaOfRectangle(l, b):
    '''Area of rectangle'''
    return f"Area: {l * b}"


def findThirdAngle(first, second):
    '''Find third Angle'''
    return f"Third Angle: {180-(first + second)}"


def factorial(x):
    '''Recursive factorial'''
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))


# Recursive factorial
'''
num = int(input("Enter number: "))
print(f"Factorial of {num} is: {factorial(num)}") 

Enter number: 8
Factorial of 8 is: 40320
'''

# Swap two numbers
'''
n1, n2 = 5, 3
print(n1, n2)

n1, n2 = n2, n1
print(n1, n2)
'''

# find Third Angle
'''
r = findThirdAngle(50, 40)
print(r) # Third Angle: 90
'''

# Area Of Rectangle
'''
area = AreaOfRectangle(8, 5)
print(area) # Area: 40
'''
