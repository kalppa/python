def myfunc(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

myfunc([1,1,1,1,2,2,3,3,3,3,4,5])

"""
Use set() method
"""

def myfunc(origin_list):
    return list(set(origin_list))
print(myfunc([9,9,9,8,8,8,]))
