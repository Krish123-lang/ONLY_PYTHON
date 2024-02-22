# l1=["1",2,3.4,"Hello", [1,2,3,4]]
#print(type(l1[0]))
# print(l1[4][1:3]) # [2, 3]

# print(len(l1[4])) # 4

# *******************************************************
# Taking input of a list, takes input separated with commas: apple ball # cat

'''
userInp=input("Enter elements: ")

l1=userInp.split()
print(l1)
'''

'''
Enter elements: apple ball cat dog
['apple', 'ball', 'cat', 'dog']
'''
# *********************************************************
'''
# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst) 
'''

'''
Enter the size of list : 3
Enter the integerelements:1 2 3 4 5
The list is: [1, 2, 3]
'''