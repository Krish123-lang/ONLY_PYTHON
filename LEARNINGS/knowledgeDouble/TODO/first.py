todoList = []

while True:
    userInput = input("enter todo: ")
    todoList.append(userInput.capitalize())

    if userInput == "exit" or userInput == "quit":
        break
    print(todoList)
