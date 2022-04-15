import jieba

data = open('生死疲劳.txt', encoding='gbk').read()
result = jieba.lcut(data, cut_all=True)

key1, key2, key3 = '月亮', '月光', '太阳'
key1_list, key2_list, key3_list = [], [], []


def word_count(key, key_list):
    key_list = []
    for item in result:
        if item == key:
            key_list.append(key)
    count_key = key_list.count(key)
    print(f'小说中 “{key}” 出现的次数是: {count_key}')
    return


print(''.center(100, '-'))
print(f'小说中指定关键词出现的统计次数如下: \n')

word_count(key1, key1_list)
word_count(key2, key2_list)
word_count(key3, key3_list)
