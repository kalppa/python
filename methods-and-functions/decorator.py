""" Return a function inside a function"""


def hello(name='Jose'):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() func inside hello!'

    print('I am going to return a function.')

    if name == 'Jose':
        return greet
    else:
        return welcome()


my_new_func = hello('Jose')
print(my_new_func())

""" Passing another function into a function"""
print('\n' *3)
print("----- Passing another function into a function ----- ")
def hello():
    return 'Hi, Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)


""" Create decorator"""
print('\n' *3)
print("----- Decorator ----- ")

def new_decorator(originial_func):
    def wrap_func():
        print('Some extra code, befor the original function')

        originial_func()
        print('Some exra code, after the original')

    return wrap_func

def func_needs_decorator():
    print(' I want to be decorated.')

func_needs_decorator()
decorated_fun = new_decorator(func_needs_decorator)
decorated_fun()
print('\n' *3)

@new_decorator
def func_needs_decorator():
    print(' I want to be decorated.')
func_needs_decorator()
