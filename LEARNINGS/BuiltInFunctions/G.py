# getattr() => returns the value of the specified attribute from the specified object.

class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, 'age')
print(x)  # 36
