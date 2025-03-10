tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)
'''
print(tup1+tup2) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup1.count(2)) # 1
print(tup1.index(4)) # 3

print(all([1, 2, 3, 4, 5])) # True
print(all([1, 2, 3, 4, 0])) # False

print(any([1, 2, 3, 4, 5]))  # True
print(any([]))  # False

print(len([1, 2, 3, 4, 5])) # 5
'''

'''
# for i, name in enumerate(tup1):
for i, name in enumerate(tup1, start=1):
    # print(f"Index({i+1}): {name}")
    print(f"Index({i}): {name}")
'''

'''
Index(1): 1
Index(2): 2
Index(3): 3
Index(4): 4
Index(5): 5
'''

'''
for ele in enumerate(tup1, start=1):
    print(ele)
'''
# ----------------------------------------
print(max([1, 2, 3, 4, 5]))  # 5
print(min([1, 2, 3, 4, 5]))  # 1
print(sum([1, 2, 3, 4, 5]))  # 15
print(sorted([1, 22, 93, 5, 50]))  # [1, 5, 22, 50, 93]
