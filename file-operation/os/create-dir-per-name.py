import os

path = os.getcwd()
print(path)

# Create a index file

content = ("dir1", "dir2", "dir3")

with open('index.txt','w') as f:
    for word in content:
       f.write(word+'\n')

# Create directories based on each line of the index file.

with open('index.txt','r') as index:
    for line in index:
        line = line.strip()
        print(line)
        try:
            os.mkdir(path +"\\"+line)
        except OSError:
            continue