from collections import Counter

val = [1, 2, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]
counter = Counter(val)
print(counter)
# Counter({4: 3, 5: 3, 1: 2, 2: 2, 3: 2})
