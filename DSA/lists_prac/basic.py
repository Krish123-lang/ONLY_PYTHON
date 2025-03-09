l1 = [1, 2, 3, 4, 5.5, True, False, "krishna", "56.5"]

# for i in l1:
#     print(i, type(i), sep=' : ')

# ============================
l2 = [6, 7, 8, 9, 10]
print(l1.index(4))  # 3

'''
print(l2.pop())  # 10

l2.append(90)
print(l2) # [6, 7, 8, 9, 90]

l2.remove(8)
print(l2) # [6, 7, 9, 90]

l2.extend(l1)
print(l2) # [6, 7, 8, 9, 10, 1, 2, 3, 4, 5.5, True, False, 'krishna', '56.5']

l2.insert(0, 10020)
print(l2) # [10020, 6, 7, 8, 9, 10]

l2.clear()
print(l2) # []

l3 = l2.copy()
print(l3) # [6, 7, 8, 9, 10]

print(l2.count(6))

l2.clear()
print(l2) # []

l2.reverse()
print(l2) # [10, 9, 8, 7, 6]

del l2[0]
print(l2) # [7, 8, 9, 10]
'''

matrix_list = [
    [1, 2, 3],
    [5, 6, 7],
    [8, 9, 10]
]
print(matrix_list[0])
print(matrix_list[1])
print(matrix_list[2])