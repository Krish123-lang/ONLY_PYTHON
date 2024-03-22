listNumbers = [20, 22, 24, 26, 28, 28, 20, 30, 24]
print("Original= ", listNumbers)

listNumbers = list(set(listNumbers))
print(listNumbers)

'''
Original=  [20, 22, 24, 26, 28, 28, 20, 30, 24]
[20, 22, 24, 26, 28, 30]
'''