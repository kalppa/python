"""break and continue can only used in the loop scenario"""

"""Break"""
#只要满足条件，退出本层循环


"""Continue"""
#满足条件时，结束本次循环，继续进行下次循环


# sum=0
# for item in range(1,51):
#     print(item)
#     if sum>100:
#         print('loop until %d'%item)
#         break #满足上述条件后退出循环
#         pass
#     sum+=item
#     pass
# print(sum)


sum=0
for item in range(1,100):
    if item%2==0: #如果是偶数，则跳过，结果是打印奇数
        continue
        pass
    print(item)
    pass
