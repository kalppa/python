import os
path = os.getcwd()
file_list = os.listdir()
python_learning_folder = os.listdir('F:\OneDrive - Cisco\docs\python\projects\learning')

print(path)
print(file_list)
print(python_learning_folder)


import shutil

# shutil.move('practice.txt','F:\OneDrive - Cisco\docs\python\projects\learning\data')

#MOVE BACK THE FILE
shutil.move('F:\OneDrive - Cisco\docs\python\projects\learning\data\practice.txt',os.getcwd())
