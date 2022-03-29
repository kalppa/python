""" Tuples are very similar to lists. However, they have one key difference - immutability.
"""

t = (1,2,3)
mylist = [1,2,3]

print(type(t))
print(type(mylist))

mylist[0] = "new"
print(mylist)

t[0] = 1
print(t)