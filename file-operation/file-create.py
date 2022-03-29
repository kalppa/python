#Create a file

with open('myfile.txt','w') as f:
    f.write('I created this file.')

with open('myfile.txt',mode='r') as f:
    print(f.read())