from functools import reduce


def greet():
    name = input("enter your name: ")
    return f"Hello, {name}"


# print(greet())
# --------------------------

def subtraction(a, b):
    return a-b

# print(subtraction(5, 3))
# --------------------------


def prime_numbers(n):
    count = 0
    x = 2
    while count < n:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                break
        else:
            print(x)
            count += 1
        x += 1


# prime_numbers(10)
'''
2 
3 
5 
7 
11 
13 
17 
19 
23 
29 
'''
# ---------------------


def fun(func, arg):
    return func(arg)


def square(x):
    return x**2


# print(fun(square, 5)) # 25
# ---------------------

def func(*args):
    for arg in args:
        print(arg)

# func(1, 2, 3, 4, 5)
# ---------------------


def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# func(name="krishna", age=23, address="Biratnagar")

'''
name: krishna
age: 23
address: Biratnagar
'''
# -------------------


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# print(factorial(5))
# -------------------
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# print(fibonacci(10))

def func(*args):
    return sum(args)


def kfuncs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print(f"the sum is: {func(1, 2, 3, 4, 5)}")
# print(kfuncs(name="krishna", age=23, address='biratnagar'))

# --------------------------------------
s = 'krishnaisawesome'
# s1=lambda func: func.upper()
s1=lambda func: func.upper()

# print(s1(s))
# ----------------------

pnz=lambda n: "Positive" if n>0 else "Negative" if n<0 else "Zero"
# print(pnz(7)) # Positive

addition = lambda a,b: a+b
# print(addition(5,3)) # 8

sq=[lambda arg=x: arg*10 for x in range(1, 11)]
# for a in sq:
#     print(a())

res=lambda x,y:(x+y, x*y)
# print(res(5,3)) # (8, 15)

# ------------------------------
# Pick items that meet a condition
n=[1,2,3,4,5]
even=filter(lambda x: x%2==0, n)
# print(list(even)) # [2, 4]

# Apply a function to every item in a list
numbers=[1,2,3,4,5]
even=list(map(lambda x: x*2, numbers))
# print(even)

# Reduce a list to a single value
num=[1,2,3,4,5]
red=reduce(lambda x,y: x*y, num)
print(red) # 120