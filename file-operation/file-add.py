#file_add

with open('test.txt',mode='r') as f:
    print(f.read())
    f.close()

with open('test.txt',mode='a') as f:
    f.write('FOUR')
with open('test.txt',mode='r') as f:
    print(f.read())
