import random

""" Basis """

# Create a new list using list()
my_list = list()

# Create a new list using []
my_list = []

# Create list with items
my_list = [1,2,3]
my_list = ['sting', 100,200,300]

print(len(my_list))

print(my_list[1])

list2 = [1,2,3]
new_list = my_list + list2
print(new_list)

list1 = [1,2,3,4,5]
print(list1.pop(0))
print(list1)

""" append list"""
# string = 'hello'
# list = []
# for letter in string:
#     list.append(letter)
# print(list)
#
# mylist = [letter for letter in string]
# print(mylist)

# def myfunc(name):
#     list = name.split()
#     reversed_list = list[::-1]
#     return reversed_list

# print(myfunc('We are ready'))

def myfunc(name):
    list = name.split()
    list.reverse()
    return  " ".join(list)

print(myfunc('We are ready'))


"""shuffle a list"""
print('----- shuffle a list -----')

mylist = [1,2,3,4,5]
random.shuffle(mylist)
print(mylist)


""" Converting """
print('---Converting Tuple to List')

device_tuple = ('1.1.1.1','username','password')
print(f'device_tuple is {device_tuple}')
device_list = list(device_tuple)
print(device_list)

print('---Converting String to List')
device_string = '1.1.1.1,username,password'
device_list = device_string.split(',')
print(device_list)
