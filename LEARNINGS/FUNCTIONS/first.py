'''
def area(r):
	#print(3.14*r*r)
	arc=3.14*r*r
	return arc

radius=float(input("Enter radius: "))
a=area(radius)
print(a)
'''

# to calculate factorial using recursion
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

num=int(input("enter the number: "))
print(f"The factorial of {num} is: {factorial(num)} ")

