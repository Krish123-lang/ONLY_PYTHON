from math import pi
import sys
# *** Even or Odd ***


def even_or_odd(num):
    "Function to analyze Even or Odd"
    if num % 2 == 0:
        return "Even"
    else:
        return "False"


# help(even_or_odd)
'''
try:
    user_input = float(input('Enter a number: '))
except Exception as e:
    print("Only numbers are allowed!")
    sys.exit()

print(even_or_odd(user_input))
'''
# -----------------------------------
# *** Multiplication Table ***


def multiplication_table(number, to_range=10):
    "Function to print Multiplication Table"
    for i in range(1, to_range+1):
        print(f"{number} x {i} = {number*i}")


# multiplication_table(5)
# -----------------------------------

def sum_of_natural_numbers():
    "sum of natural numbers"
    sum = 0
    for i in range(10):
        sum += i
    print(f"Sum of natural numbers: {sum}")


# sum_of_natural_numbers()
# -----------------------------------

def swap_two_numbers(x, y):
    "Swap Two numbers"
    x, y = y, x
    print(x, y, sep=', ')


# swap_two_numbers(4, 3)
# -----------------------------------

def opposite_dice(n):
    "To print the opposite side of the dice"
    oppo = 7-n
    print(oppo)


# opposite_dice(6)
# -----------------------------------

def simple_interest(p, t, r):
    return (p*t*r)/100


# print(simple_interest(500, 7, 13))
# -----------------------------------


def area_of_circle(r=0):
    return f"Area of circle: {pi*r*r:.2f}"


# print(area_of_circle(5))
