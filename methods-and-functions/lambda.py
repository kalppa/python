def square(num):
    result = num ** 2
    return result
print(square(3))

def square(num):
    return  num ** 2
print(square(3))


square = lambda num: num **2
print(square(5))

mynums = [1,2,3,4,5]
list(map(lambda num:num**2,mynums))
for n in list(map(lambda num:num**2,mynums)):
    print(n)
