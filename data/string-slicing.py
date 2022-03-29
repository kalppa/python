mystring = 'abcdefghijk'

# Indexing
print(mystring[2])

# Slicing from c to the end.
print(mystring[2:])

# Stop - from index 0 to 2
print(mystring[:3])

# From index3 to index6
print(mystring[3:6])

# Include all
print(mystring[::])

# Step - Jumping in the step size of 2
print(mystring[::2])

# Reversing
print(mystring[::-1])


# def myfunc(name):
#     first_letter = name[0]
#     inbetween = name[1:3]
#     fourth_letter = name[3]
#     rest = name[3:]
#     return first_letter.upper + inbetween + fourth_letter.upper + rest

# print(myfunc('macdonald'))

def myfunc(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

print(myfunc('macdonald'))

