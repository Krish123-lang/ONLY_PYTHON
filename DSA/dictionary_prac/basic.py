dict1 = {
    'name': 'krishna',
    'age': 23,
    'address': 'biratnagar'
}

dict1['isGamer'] = False
dict1['name'] = "Bob the builder"

# del dict1['name'] # removes value with the key: name
print(dict1.get('name')) # Bob the builder
print(dict1.keys()) # dict_keys(['name', 'age', 'address', 'isGamer'])
print(dict1.items()) # dict_items([('name', 'Bob the builder'), ('age', 23), ('address', 'biratnagar'), ('isGamer', False)])
# print(dict1.popitem()) # ('isGamer', False) => removes the last key: value pair from the dictionary

# dict2 = dict1.copy()
# print(dict2)

# print(dict1.setdefault('age')) # 23

'''
dict1.pop('isGamer')
print(dict1) # remove isGamer from the dictionary

dict1.clear()
print(dict1) # {}
'''

# print(dict1)
# for a, b in dict1.items():
#     print(f"{a}: {b}")