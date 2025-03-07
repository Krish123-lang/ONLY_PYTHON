# mydict = {}
# mydict["name"] = "krishna"

# def greet():
#     return f"Hello, {mydict['name']}"

# print(greet())
# ===============================

# person = {
#     {
#         'name': 'krishna',
#         'roll': 11,
#         'class': 10
#     },
#     {
#         'name': 'Bob',
#         'roll': 1,
#         'class': 9
#     },
#     {
#         'name': 'John',
#         'roll': 3,
#         'class': 8
#     }
# }
person = {
    'name': 'John',
    'roll': 3,
    'class': 8
}

# for key in person.keys():
#     print(key)

animals = 'lions'
# print(f"There are {animals!r} in my house")
# print(f"the king of the jungle is: {animals=}")

'''
There are 'lions' in my house
the king of the jungle is: animals='lions'
'''

'''
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except Exception as e:
        print(e, "Please try again!")
'''
# =====================================
x, y, *z = 1, 2, 3, 4
print(x, y, z) # 1 2 [3, 4]
