"""
*args and **kwargs - stands for arguments and keyword arguments
"""


# treat *args as a tuple,no matter how many args
# *args - args can be any words, but by convention, it usually uses args
# def myfunc(*args):
#     return sum(args) * 0.05
#
# print(myfunc(40, 60, 100))
#
#
# # **kwargs - indicates any lists
# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')
#
# print(myfunc(fruit='apple', veggie='lettuce'))


def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dogs')

def myfunc(*args):
    return sum(args)
print(myfunc(10,15))