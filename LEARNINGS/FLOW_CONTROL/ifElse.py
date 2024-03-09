num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))

if(num1>num2 and num1>num3):
	print("Num1 is greater")

elif(num2>num1 and num2>num3):
	print("Num2 is greater")

else:
	print("Num3 is greater")