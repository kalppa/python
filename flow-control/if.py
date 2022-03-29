""""""

"""单分支流程"""

"""
条件表达式：
    1.  比较运算符
    2.  逻辑运算符
    3.  复合的运算符
"""
#
# score=60
#
# if score <=60:  #判断条件
#     print('Failed')
#     pass    #空语句，跳出循环
#
# print('Code Finished')

"""双分支流程"""

# score=80
#
# if score >= 60:
#     print('Passed')
#     pass
# else:
#     print('Failed')
#     pass

"""多分支流程"""
    # 多个elif，而且每个分支是互斥的
    # 只要满足其中一个分支就退出本层if语句的结构
    # 至少有两种以上的条件可以选择
    # elif必须跟上一个条件
    # 最后的else是optional，不是必须
#
# score=int(input('Please input your score:'))
#
# if  score>90:
#     print('A')
#     pass
# elif score>=80:
#     print('B')
#     pass
# elif score>=70:
#     print('C')
#     pass
# elif score>=60:
#     print('D')
#     pass
# else:
#     print('Failed')
#     pass
#

# import random   #随机函数
# person=int(input('请出拳：[0：石头 1：剪刀 2：布]'))
# computer=random.randint(0,2)
#
# print('Person={}' .format(person))
# print('Computer={}' .format(computer))
#
# if person==0 and computer==1:
#     print('We win')
#     pass
# elif person==1 and computer==0:
#     print('Computer Win')
#     pass
# elif person==computer:
#     print('SAME SAME!')
#     pass
# elif person>2:
#     print('Wrong Input')
#     pass
# else:
#     print('Game Over')
#     pass



"""if else嵌套"""
#if else结构可以多层嵌套




st = 'Print only the words that start with s in this sentence'
print(st.split())
for words in st.split():
    if words[0] == 's':
        print(words)



