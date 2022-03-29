""" Inheritance """
""" Inheritance means a derived class can inherit methods from a base class"""

# Create a base class
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

myanimal = Animal()
myanimal.eat()

# Create a new class inherit the methods of base class.
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

mydog = Dog()
mydog.eat()
