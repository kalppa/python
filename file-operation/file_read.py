# File Read

myfile = open("test.txt")
# print(myfile.read())
# print (myfile.read(5))        # Read specific letters.
# print (myfile.readline())     # Only read one line.
# print (myfile.readlines())    # Each line as a list.
myfile.close()

file1 = open("C:\\Users\\chris\\Downloads\\test.txt")
file1.close()
# For Windows, you need to use double \ so python doesn't treat
# the second \ as an escape character.
# print(file1.readlines())

"""
Use with open method to open a file, then we don't need to close the file.
"""
with open('test.txt') as my_new_file:
    contents = my_new_file.readlines()
    print(contents)