password = input("enter password: ")
confirmPassword = input("Confirm password: ")

while password != confirmPassword:
    print("Try Again !")
    confirmPassword = input("Confirm password: ")

else:
    print("Hi there")
