"""语法"""
'''
for 临时变量 in 字符串，列表等
    执行代码块
'''


"""pass - Do nothing, usually used as a placeholder"""
# for i in range(1,100):
#     print(i,end=' ')
#     pass             # Do nothing, usually used as a placeholder

""" continue - skip this condition
continue: Goes to the top of the closest enclosing loop.
"""
# for letter in 'Sammy':
#     if letter == 'a':
#         continue
#     print(letter)

""" break - stop the loop"""
for letter in 'Sammy':
    if letter == 'a':
        break
    print(letter)

