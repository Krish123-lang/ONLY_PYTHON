'''
this program takes two angles input from user and prints the third angle
'''

firstAngle = int(input("Enter first angle: "))
secondAngle = int(input("Enter second angle: "))

thirdAngle = 180-(firstAngle+secondAngle)
print(f"The third angle is: {thirdAngle}")

'''
Enter first angle: 60
Enter second angle: 20
The third angle is: 100
'''