
# total_finding = 0
# with open('生死疲劳.txt', 'r', encoding='GBK') as f:
#     for num, line in enumerate(f, 1):
#         if '月光' in line:
#             total_finding+=1
#             print('Found "月光" at line:', num )
#             print(total_finding)

# import jieba
#
# str = '数据分析师数据库管理员数据架构师数据挖掘工程师'
#
# result1 = jieba.cut(str)
# print(type(result1))
# print(result1)
# print('/'.join(result1))
#
# print(''.center(100, '-'))
# result2 = jieba.lcut(str)
# print(type(result2))
# print(result2)

from pprint import pprint

data = open('a.txt', encoding='utf-8').read()
# data = open('a.txt', encoding='gbk').read()
# print(type(data))
# pprint(data)

#
# import jieba
#
# result = jieba.lcut(data)
# key1 = '月光'
# key2 = '月亮'
# key_list1 = []
# key_list2 = []
#
#
# def word_count(key, key_list):
#     key_list = []
#     for item in result:
#         if item == key:
#             key_list.append(key)
#     print(key_list)
#     return
#
# word_count(key1, key_list1)
# word_count(key2, key_list2)

from collections import Counter
import jieba
import pprint

data = open('a.txt', encoding='utf-8').read()
result = jieba.lcut(data, cut_all=True)

print(result)

print(type(Counter(result)))
print(Counter(result))

print(Counter(result)['月光'])