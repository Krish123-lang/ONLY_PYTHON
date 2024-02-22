l1=[1,2,3,4,5]
# l1[2]="Hello" # [1, 2, 'Hello', 4, 5] => 3 has been replaced by 'Hello'

l1[0:3]=["one", "two", "three", "four"] # replaces 1,2,3 by the words and adds "four"
print(l1) # ['one', 'two', 'three', 'four', 4, 5]