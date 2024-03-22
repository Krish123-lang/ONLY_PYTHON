from operator import index


l1 = []

for i in range(1, 11):
    l1.append(i)

# print(l1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
# l1.clear() # => removes all items from the list
# print(l1) # []
'''
# ---------------------------------------------------
'''
l2=l1.copy() => returns the copy of the list
print(l2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
# ---------------------------------------------------

'''
count() => Returns the number of elements with the specified value
print(l1.count(4)) # 1 => becoz 1 is only present once in the list
'''
# ---------------------------------------------------

'''
extend() => Add the elements of a list (or any iterable), to the end of the current list

a1 = ["a", "b", "c"]
a2 = ["d", "e", "f"]

# a1.extend(a1) # ['a', 'b', 'c', 'a', 'b', 'c']
a1.extend(a2) # ['a', 'b', 'c', 'd', 'e', 'f']
print(a1)

'''
# ---------------------------------------------------

'''
index()=>Returns the index of the first element with the specified value

b = ["a", "b", "c", "b"]
print(b.index("b")) # 1 as it only indexes the first occurence
'''
# ---------------------------------------------------

'''
insert() => Adds an element at the specified position, without replacing the existing element
c = [1, 2, 3, 4, 5]
c.insert(1, 0)
print(c) # [1, 0, 2, 3, 4, 5]

d = [1, "a", "3.3", 43.2, "hello"]
d.insert(2, "world")

print(d) # [1, 'a', 'world', '3.3', 43.2, 'hello']
'''
# ---------------------------------------------------

'''
pop() => Removes the element at the specified position(index) or from the end

e = [1, 2, 3, 4, 5]
e.pop(2)  # [1, 2, 4, 5] => removes three from the list
# e.pop()
print(e)  # [1, 2, 3, 4] => removes an element from the end
'''
# ---------------------------------------------------

'''
remove() => removes the first occurrence of the element with the specified value.

f = ["apple", "ball", "cat"]
f.remove("ball")
print(f) # ['apple', 'cat']

'''
# ---------------------------------------------------

'''
reverse() => reverses the order of the list

g = ["a", "b", "c"]
g.reverse()
print(g) # ['c', 'b', 'a']
'''
# ---------------------------------------------------

'''
sort() => sorts the list ascending by default.

h = ["donkey", "ball", "abacus"]
h.sort()
h.sort(reverse=True)  # ['donkey', 'ball', 'abacus']
print(h)  # ['abacus', 'ball', 'donkey']

'''
# ---------------------------------------------------