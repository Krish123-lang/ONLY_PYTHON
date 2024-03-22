# for i in range(1, 11):
#     print(i)

# sum of numbers

# sum = 0
# for i in range(1, 10):
#     sum += i
#     print(f"{i}")

# print(sum)

'''
l1 = [1, 2, 3, 4, 5]
l2 = []

for i in l1:
    sq = i**2
    l2.append(sq)

print(l2)
'''
# ******************************

'''
def cube_numbers(numbers):
    return [num ** 3 for num in numbers]


def main():
    numbers = []
    while True:
        user_input = input("Enter a number or type 'exit' to quit: ")
        if user_input.lower() in ('exit', 'quit'):
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or type 'exit' to quit.")

    if numbers:
        cubes = cube_numbers(numbers)
        print("Cubes of the given numbers:", cubes)
    else:
        print("No numbers were provided.")


if __name__ == "__main__":
    main()
'''