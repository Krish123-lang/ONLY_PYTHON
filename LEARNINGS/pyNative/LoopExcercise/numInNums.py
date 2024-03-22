'''
1. Run while loop till number != 0
2. In each iteration of loop
    Reduce the last digit from the number using floor division ( number = number // 10)
    Increment counter by 1
'''

num=int(input("Enter a number: "))

counter = 0

while num != 0:
    num = num//10
    counter += 1

print(counter)


'''
Enter a number: 454545
6
'''