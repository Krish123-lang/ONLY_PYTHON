import random

choices = ['rock', 'paper', 'scissor']
mapping = {
    '1': 'rock',
    '2': 'paper',
    '3': 'scissor',
    '4': 'q',
}

def separator():
    print('-'*60)


while True:
    user_action = input('''
    1. Rock
    2. Paper
    3. Scissor
    4. q to quit
    ''').lower().strip()

    user_action = mapping.get(user_action, user_action)

    if user_action == 'q':
        print('see you again!')
        separator()
        break

    if user_action not in choices:
        print('Invalid choice! 1,2,3,4 only allowed.')
        separator()
        continue

    computer_action = random.choice(choices)

    if user_action == computer_action:
        print(f"{user_action.capitalize()} == {computer_action.capitalize()}! It's a tie.")
        separator()

    elif (user_action == 'rock' and computer_action == 'scissor') or (user_action == 'paper' and computer_action == 'rock') or (user_action == 'scissor' and computer_action == 'paper'):
        print('You won!')
        
    else:
        print('Computer won!')
