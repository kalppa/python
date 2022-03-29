"""
Sets are unordered collections of unique elements.
Meaning there can only be one representative of the same object.
"""

myset = set()
myset.add(1)
print(myset)

myset.add(2)
print(myset)
myset.add(2)  # cannot add 2 the second time, set are unique, it won't repeat.
print(myset)

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
set(mylist)
print(set(mylist))  # Can be used to remove duplicated items.
