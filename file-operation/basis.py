file_in = open('in.txt','r')
file_out = open('out.txt','w')

x = file_in.read(1)
print(x)
x = file_in.read(1)
print(x)
file_out.write(x)
x = file_in.read(1)
print(x)
x = file_in.read(1)
print(x)
file_out.write(x)
file_in.close()
file_out.close()
