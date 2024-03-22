'''
1. The number must be divisible by five
2. If the number is greater than 150, then skip it and move to the next number
3. If the number is greater than 500, then stop the loop
'''

num = [12, 75, 150, 180, 145, 525, 50]

for i in num:
    if (i > 500):
        break

    if (i > 150):
        continue

    if (i % 5 == 0):
        print(i)

'''
75
150
145
'''
