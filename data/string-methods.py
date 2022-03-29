s = 'hello world'

s.capitalize()
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.find('o'))
x = 'Hi this is a string'
print(x.upper())

""" Split """
print(x.split())  # Split to a List
print(x.split('i'))  # Split to a List of letters by i

my_string = "router, switch, access point"
# By default, string is split by space.
print(my_string.split())

# Can use ',' as a delimiter.
print(my_string.split(','))


""" Strip """
# You can use strip() to remove white space from the beginning or end of a string
# You can not only remove the white space, but also remove the '\n'

device2 = my_string.split(',')[1]
print(device2)

device2 = device2.strip()
print(device2)

""" len() """
print(len(my_string))
