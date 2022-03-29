
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name):

        # Attributes
        # We take in the argument: breed
        # Assign it using self.attribute_name: self.bread
        self.breed = breed
        self.name = name

    # OPERATIONS/ACTIONS ---> Methods
    # number is user defined argument
    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog(breed='Lab', name='Sammy' )

print(my_dog.breed, my_dog.name)
my_dog.bark(10)



