import math
PI = math.pi


def Diameter(radius):
    return 2*radius


def Circumference(radius):
    return 2*PI*radius


def Area(radius):
    return PI*radius*radius


radius = float(input("enter radius: "))

diameter = Diameter(radius)
circumference = Circumference(radius)
area = Area(radius)

print(f"Diameter: {diameter}\nCircumference: {circumference:.2f}\nArea: {area:.2f}")

'''
We use f'{area:.2f}' to print only the two digits after (.). like in c and c++ we used %.2f
'''

'''
enter radius: 7
Diameter: 14.0
Circumference: 43.98
Area: 153.94
'''