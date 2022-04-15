
"""" Capitalization """
s = 'ada lovelace'
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

""" Find the position of a character """
# print(s.find('o'))


""" Convert string to list """
print(s.split())  # Split to a List
print(s.split('l'))  # Split to a List of letters by i

my_string = "router, switch, access point"
# By default, string is split by space.
print(my_string.split())

# Can use ',' as a delimiter.
print(my_string.split(','))


""" Strip """
# You can use strip() to remove white space from the beginning or end of a string
# strip() removes both the left and right end whitespaces
# Only removed temporarily, if you want to remove it permanently, need to reassign the value to a new variable.
# You can not only remove the white space, but also remove the '\n'

device2 = my_string.split(',')[1]
print(device2)

device2 = device2.strip()
print(device2)

# Move the left and right whitespace
# Only remove temporarily.
s = ' python '
print(s.rstrip())
print(s.lstrip())
print(s)

""" len() """
print(len(my_string))
