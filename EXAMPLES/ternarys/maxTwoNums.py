a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

print("a is greater" if (a > b and a > c) else ("b is greater" if b > a and b > c else "c is greater"))

'''
first number: 56
second number: 34
third number: 23
a is greater

--------------------

first number: 43
second number: 667
third number: 34
b is greater

---------------------

first number: 45
second number: 23
third number: 45984
c is greater
'''
