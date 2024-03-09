# filter() => Use a filter function to exclude items in an iterable object
'''
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x)
'''
'''
18
24
32
'''
# *****************************************************************

# print(float(4)) # 4.0