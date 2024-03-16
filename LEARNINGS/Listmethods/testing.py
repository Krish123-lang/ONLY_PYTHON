l1 = []

while True:
    userInp = input("Enter todo: ")
    l1.append(userInp)

    if userInp == "exit":
        l1.pop()
        break

print(l1)
