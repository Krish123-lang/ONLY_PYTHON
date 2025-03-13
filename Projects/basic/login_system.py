username = input("enter username: ")
email = input("enter email: ")
password = input("enter password: ")
confirm_password = input("Confirm password: ")

if password == confirm_password:
    print('you are registered successfully!')
else:
    print('Password does\'nt match!')
