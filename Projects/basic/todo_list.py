todo_list = []


def separator():
    print('-'*60)


def add_item():
    print('Add item (press q to quit):')
    while True:
        add_to_the_list = input('>').strip()
        if add_to_the_list.lower() == 'q':
            break
        if not add_to_the_list:
            print('cannot add empty item!')
            continue
        todo_list.append(add_to_the_list)
    print(f"Todo Items: {todo_list}")
    separator()


def display_item():
    if len(todo_list) > 0:
        print(todo_list)
        item_to_display = input('enter the item to display: ')
        if item_to_display in todo_list:
            item_index = todo_list.index(item_to_display)
            print(f"Item detail: {todo_list[item_index]}")
            separator()
        else:
            print('Please enter a item that is in todo list!')
            separator()
    else:
        print('Todo is empty!')
        separator()


def edit_item():
    print(todo_list)
    item_to_edit = input('enter the item to edit: ')
    if item_to_edit in todo_list:
        item_index = todo_list.index(item_to_edit)
        item_to_replace = input('edit the item: ')
        todo_list[item_index] = item_to_replace
        print(todo_list)
    else:
        print('Please enter a item that is in todo list!')
        separator()


def delete_item():
    print(todo_list)
    item_to_delete = input('enter the item to delete: ')
    if item_to_delete in todo_list:
        item_index = todo_list.index(item_to_delete)
        confirm = input(f"Are you sure you want to delete {item_to_delete}? (yes/no)").lower().strip()
        if confirm == "yes":
            del todo_list[item_index]
            print(f"{item_to_delete} has been deleted!")
            print(todo_list)
            separator()
        else:
            print("Deletion cancelled!")
            separator()
    else:
        print('Please enter a item that is in todo list!')
        separator()


def main():
    while True:
        try:
            print("""
            *** Options ***
            1. Add item
            2. Display item
            3. Edit item
            4. Delete item
            5. Exit
            """)

            option_input = int(input('Select an option: '))

            if option_input == 1:
                add_item()

            elif option_input == 2:
                display_item()

            elif option_input == 3:
                edit_item()

            elif option_input == 4:
                delete_item()

            elif option_input == 5:
                print('Bye! Please visit again.')
                break

            else:
                print("Invalid option!")
        except ValueError:
            print('*** Please enter only numeric options from above! ***')
            continue

main()