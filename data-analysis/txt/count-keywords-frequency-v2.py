
# Read the novel as a variable
data = open('生死疲劳.txt', encoding='gbk').read()

# Use jieba module to split Chinese characters
import jieba

# Use 'lcut' method to convert all the possible words into a List.
# Use option 'cut_all=True' to list all the possible combinations.
result = jieba.lcut(data, cut_all=True)

# Define the target keyword and keyword_list for the function.
key1 = '月亮'
key1_list = []
key2 = '月光'
key2_list = []
key3 = '太阳'
key3_list = []

# Define the function.
def word_count(key, key_list):
    key_list = []
    for item in result:
        if item == key:
            key_list.append(key)
    count_key = key_list.count(key)
    print(f'The total count of {key} is: {count_key}')
    return

print(''.center(100, '-'))
print(f'The analysis of specific words in the novel is listed below: \n')

word_count(key1, key1_list)
word_count(key2, key2_list)
word_count(key3, key3_list)
