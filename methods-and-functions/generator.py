""" range() is a generator function"""
# The advantages of generator are that we don't need to store the list in memory.


print("-----create my own generator-----")

def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)