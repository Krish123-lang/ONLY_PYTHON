import random

'''
# returns a random floating point number
print(random.random())

# returns a random single element from the sequence
print(random.choice([1, 2, 3, 4, 5]))

# returns a single integer value from the given range 1 to 3 in this case
print(random.randint(1, 3))

# returns a single integer value from the given range 1 to 3 in this case. but doesn't include the last number
print(random.randrange(1, 3))

# returns a random float number between the given range
print(random.uniform(1.5, 5.5))

# returns two random elements from the sequence, the numbers of elements depends on the value of 'k'
print(random.sample([1, 2, 3, 4, 5], k=2))  # [5, 2]

# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
mylist = [1, 3, 5, 2, 4]
random.shuffle(mylist)
print(mylist) # [4, 1, 3, 2, 5]
'''

'''
chance = 3
correct_number = random.randint(1, 10)
print(correct_number)

while chance >= 1:
    print(f"You have {chance} chances left")
    user_input = int(input('enter a number between 1 to 10: '))
    if user_input == correct_number:
        print('you won the game!')
        break
    else:
        chance -= 1
        print(f'Try Again! You have {chance} chance left.')
        if chance == 0:
            print('You lose! Wake up to reality.')
            break
'''

'''
enter a number: 3
you won the game!
'''

# ===============================
MAX_CHANCES = 3
LOWER_LIMIT = 1
UPPER_LIMIT = 10

target_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
# print(target_number)

for chance in range(MAX_CHANCES, 0, -1):
    print(f"You have {chance} chance(s) left!")

    try:
        user_input = int(input(f'Enter a number between {LOWER_LIMIT} and {UPPER_LIMIT}: '))
    except ValueError:
        print("please enter a valid number")
        continue

    if user_input >= LOWER_LIMIT and user_input <= UPPER_LIMIT:
        if user_input == target_number:
            print("You won the game!")
            break
        else:
            print('Try again!')

if user_input != target_number:
    print(f'You lost the game! The correct number was: {target_number}')
