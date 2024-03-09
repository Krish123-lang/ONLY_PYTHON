'''
this program takes two input from user as temp in Celsius and Farenheit and converts them into Celsius and Farenheit
'''

tempC = float(input("Enter the temperature in Celsius: "))

tempF = float(input("Enter the temperature in Farenheit: "))


cTof = (tempC*(9/5))+32
fToc = (tempF-32)*(5/9)

print(f"The temperature in Farenheit is: {cTof}")
print(f"The temperature in Celsius is: {fToc}")


'''
Enter the temperature in Celsius: 37
Enter the temperature in Farenheit: 98
The temperature in Farenheit is: 98.60000000000001
The temperature in Celsius is: 36.66666666666667
'''