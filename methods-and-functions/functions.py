"""
By conventions, functions use Snake Casing.
def name_of_function():  # Snake Casing - lower case letters with underscores.
name_of_function()  # call the function by name.

"""


def say_hello():
    print("hello")

say_hello()

def say_hello(name):
    print(f'Hello {name}')

say_hello('chris')

def say_hello(name='default'):  # Assign a default value to the argument.
    print(f'Hello {name}')
say_hello()


def sum(num1,num2):
    return num1+num2  # return save the result as a variable.
sum = sum(1,2)
print(sum)

def tell_a_number_is_even_or_odd(num):
    if num%2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
tell_a_number_is_even_or_odd(110)

