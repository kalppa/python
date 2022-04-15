
# Read the novel as a variable
data = open('生死疲劳.txt', encoding='gbk').read()

# Use jieba module to split Chinese characters
import jieba

# Use 'lcut' method to convert all the possible words into a List.
# Use option 'cut_all=True' to list all the possible combinations.
result = jieba.lcut(data, cut_all=True)

# Analysis how many times the word '月亮' shows in the novel and then fill all the word in key1_list.
key1 = '月亮'
key1_list = []
for word in result:
    if word == key1:
        key1_list.append(key1)

count_key1 = key1_list.count(key1)


# Analysis how many times the word '月光' shows in the novel and then fill all the word in key1_list.
key2 = '月光'
key2_list = []
for word in result:
    if word == key2:
        key2_list.append(key2)

count_key2 = key2_list.count(key2)

# Analysis how many times the word '明月' shows in the novel and then fill all the word in key1_list.
key3 = '明月'
key3_list = []
for word in result:
    if word == key3:
        key3_list.append(key3)

count_key3 = key3_list.count(key3)

# Analysis how many times the word '太阳' shows in the novel and then fill all the word in key1_list.
key4 = '太阳'
key4_list = []
for word in result:
    if word == key4:
        key4_list.append(key4)

count_key4 = key4_list.count(key4)

print(''.center(100,'-'))
print(f'The analysis of specific words in the novel is listed below: \n')
print(f'The total count of {key1} is: {count_key1}')
print(f'The total count of {key2} is: {count_key2}')
print(f'The total count of {key3} is: {count_key3}')
print(f'The total count of {key4} is: {count_key4}')
