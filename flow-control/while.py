"""while"""
#主要适用于不知道明确的循环次数，需要判断条件来决定是否结束循环，而for主要适用于已知的循环次数

# while循环的特点：
#     1.有初始值
#     2.条件表达式
#     3.变量循环体内的计数变量自增自减，否则会造成死循环
#
# 目的：
# 为了将相同或相似的代码变得更加简洁，使代码可以重复复用

#打印1-100

# index=1
# # print(index)
#
# while index<=100:
#     print(index)
#     index+=1
#     pass

"""打印99乘法表"""
#正序
# row=1
# while row<=9:
#     col=1
#     while col<=row:
#         # print('%d*%d=%d'%(row,col,row*col)) #每一次执行打印一行，默认print完换行
#         print('%d*%d=%d' % (row, col, row * col),end=' ')  # 指定执行完不换行而是用空格分开
#         col+=1
#         pass
#     print()
#     row+=1
#     pass

#倒序

# row=9
# # while row>=1:     #下面一行也可以，但是要注意设定row得>=1，不然row自减会永远小于9，就跳不出循环了
# while row<=9 and row>=1:
#     col=1
#     while col<=row:
#         # print('%d*%d=%d'%(row,col,row*col)) #每一次执行打印一行，默认print完换行
#         print('%d*%d=%d' % (row, col, row * col),end=' ')  # 指定执行完不换行而是用空格分开
#         col+=1
#         pass
#     print()
#     row-=1
#     pass

"""打印直角三角形"""
#正序
# row=1
# while row<=7:
#     j=1
#     while j<=row:
#         print('*', end='')
#         j+=1
#         pass
#     print()
#     row+=1
#     pass

#反序
# row=7
# while row>=1:
#     j=1
#     while j<=row:
#         print('*', end='')
#         j+=1
#         pass
#     print()
#     row-=1
#     pass


"""打印等腰三角形"""
row=1
while row<=5:
    j=1
    while j<=5-row:
        print(' ',end='')
        # print('#',end='')
        j+=1
        pass
    k=1
    while k<=2*row-1:
        print('*',end='')
        k+=1
        pass
    print()
    row+=1
    pass
