"""
Operators tha allow you t convey True or False
"""

# print(1 > 2)
# print(1 == 2)
#
# b = None # Use None as a placeholder.
# print(b)

"""
Logical Operators

"""
#
# print(1 < 2 and 2 < 3)
# print(1 < 2 and 2 > 3)
#
# print(100 == 1 or 2 == 2)

print('x' in 'taxi')


def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(myfunc(6,19))
