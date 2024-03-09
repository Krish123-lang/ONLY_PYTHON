# delattr() => The delattr() function will delete the specified attribute from the specified object.
'''
class Person:
    name = "Apple"
    age = 23
    address = "Garden"


delattr(Person, 'age')

'''

# ******************************************************************
# dict() => The dict() function creates a dictionary.
'''
mydict = dict(name="John", age=32, address="Pluto")
print(mydict) #{'name': 'John', 'age': 32, 'address': 'Pluto'}
'''
# ******************************************************************

# dir() => The dir() function returns all properties and methods of the specified object, without the values.

'''
class Person:
    name = "Apple"
    age = 23
    address = "Garden"


print(dir(Person))
'''
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'address', 'age', 'name']
'''
# ******************************************************************

# divmod() => The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
'''
print(divmod(4, 2)) # (2, 0)
print(divmod(9, 2)) # (4, 1)
'''
# ******************************************************************
