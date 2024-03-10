import random

'''
# seed() => used to initialize the random number generator.
random.seed(10)
print(random.random())
'''
# ------------------------------------------------------------

# randrange() => Returns a random number between the given range
# print(random.randrange(1, 50))

# ------------------------------------------------------------

# randint() =>	Returns a random number between the given range
# print(random.randint(1, 10))

# ------------------------------------------------------------

'''
The choice() method returns a randomly selected element from the specified sequence.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
'''
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(list1))

x = 'welcome'
print(random.choice(x))
'''

# ------------------------------------------------------------

'''
The choices() method returns a list with the randomly selected element from the specified sequence.
You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
'''
'''
mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights=[10, 1, 1], k=14))
'''

# ------------------------------------------------------------

# shuffle() => method takes a sequence, like a list, and reorganize the order of the items.

'''
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)
'''

# ------------------------------------------------------------

# sample() => method returns a list with a specified number of randomly selected items from a sequence.
'''
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=3))
'''

# ------------------------------------------------------------
# random() => Returns a random float number between 0 and 1
# print(random.random())
# ------------------------------------------------------------

# uniform() => method returns a random floating number between the two specified numbers (both included).
# print(random.uniform(20, 60))

# ------------------------------------------------------------