# append function adds an element at the end of the list
'''
l1=[]

for i in range(1,11):
    l1.append(i)

l1.append((20, 21))
l1.append([22, 23])
l1.append("Hello")
print(l1)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

'''
# insert() function is used to add an element at the desired position
a=[1,2,3,4]
#a.insert(0, "Hello") # ['Hello', 1, 2, 3, 4]
a.insert(2, (10,11)) # [1, 2, (10, 11), 3, 4]
print(a)
'''

'''
b=[1,2,3,4]
b1=[10,11,12,13]

#b.extend(["apple", "ball", 4,5,6]) # [1, 2, 3, 4, 'apple', 'ball', 4, 5, 6]

b.extend(b1) # [1, 2, 3, 4, 10, 11, 12, 13]
print(b)
'''