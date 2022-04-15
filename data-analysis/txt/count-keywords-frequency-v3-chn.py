# 此程序可以用于分析统计文本或者小说中某个词出现的频率

# 使用open函数将小说的内容赋值给变量data
data = open('生死疲劳.txt', encoding='gbk').read()

# 使用jieba模块来进行中文分词，因为为中文跟英文不一样，英文不同的单词间有空格作为区分，中文是连在一起的，所以需要专用的分词模块
import jieba

# 使用lcut method将data中的中文字进行词语切分
# lcut切分词语有多种方式，使用option 'cut_all=True'最大程度上去切分词语
result = jieba.lcut(data, cut_all=True)

# 定义要统计的关键字变量
# 为每一个关键字定义一个空的列表，将来每查找到一个关键字就往列表里填一次，最后统计列表中元素的数量，也就是关键字总共出现的次数了
key1 = '月亮'
key1_list = []
key2 = '月光'
key2_list = []
key3 = '太阳'
key3_list = []


# 写一个函数进行循环查找和统计
# 此函数有2个参数，一个是需要查找的关键字(key1, key2, key3...)，另一个是关键字对应的空列表(key1_list, key2_list, key3_list)

def word_count(key, key_list):
    # 定义key_list为一个空列表，这里的key_list是一个函数变量，根据后面的参数输入来对应到具体的变量，比如后面执行函数时填入key2_list这才是
    # 实际的变量
    key_list = []

    # 使用一个变量在result这个已经切分了词语的列表中进行循环查找，每次查找一个词
    for item in result:

        # 如果找到的词与我们想要的词匹配，这里的key也是函数变量具体会根据后面的参数输入对应到我们想找的词，比如我们输入key1，那这里就是'月亮'
        if item == key:
            # 如果匹配到就将这个词添加到空列表中
            key_list.append(key)

    # 使用count()方法统计列表中所有元素的数量
    count_key = key_list.count(key)
    print(f'小说中 “{key}” 出现的次数是: {count_key}')
    return


# 显示结果
# 打印100个'-'作为分隔符，显示用途
print(''.center(100, '-'))
print(f'小说中指定关键词出现的统计次数如下: \n')

# 调用函数
word_count(key1, key1_list)
word_count(key2, key2_list)
word_count(key3, key3_list)
