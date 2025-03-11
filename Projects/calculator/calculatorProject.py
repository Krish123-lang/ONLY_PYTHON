# print("""
#                                                 *** Calculator App ***
#       """)
# number_of_operands = int(input('Enter the number of operands: '))

# iterating_number_of_operands = 0
# operands = []
# for _ in range(number_of_operands):
#     operand = float(input('Enter the operands: '))
#     operands.append(operand)

# # print(sum(operands))


# def addition(*args):
#     return sum(operands)


# print('---------------------------------------------------------')
# print(f"The sum of the operands is: {addition(operands)}")
# print('---------------------------------------------------------')

# ===================================
import sys


def addition(x, y):
    return x+y


def subtraction(x, y):
    return x-y


def multiplication(x, y):
    return x*y


def division(x, y):
    return x/y if y != 0 else "You are not allowed to divide by zero"


try:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
except Exception as e:
    print(f"Please enter number only! \nError: {e}")
    sys.exit()

operation = input(""" 
Enter the operation you want to perform:
1. Add
2. Subtract
3. Multiplication
4. Divide
> """).strip().lower()


operations = {
    "1": addition, "add": addition, "addition": addition, "+": addition, "sum": addition,
    "2": subtraction, "subtract": subtraction, "subtraction": subtraction, "-": subtraction, "difference": subtraction, "minus": subtraction,
    "3": multiplication, "multiply": multiplication, "multiplication": multiplication, "*": multiplication, "product": multiplication,
    "4": division, "divide": division, "division": division, "/": division
}

if operation in operations:
    result = operations[operation](a, b)
    print(f"Result: {result:.2f}")
else:
    print("Invalid operator!")

# ========================================
'''
Enter the value of a: 989.34343434
Enter the value of b: 34.345428
 
Enter the operation you want to perform:
1. Add
2. Subtract
3. Multiplication
4. Divide
> 4
Result: 28.81
'''
# ========================================
