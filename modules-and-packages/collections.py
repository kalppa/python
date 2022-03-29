from collections import Counter

mylist = [1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]

print(Counter(mylist))
print('\n'*2)

print('----- Count how many words in a sentence.-----')
s = "Learn Python like a Professional Start from the basics and go all the way to creating your own applications and games"
print(Counter(s.split()))
print('\n'*2)

print('----- count the most common letters -----')
letters = 'aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbccccccccccdddddddddddddddddddddddzzzzzzzzzzzzzzzzzzzzzz'
c = Counter(letters)
print(c)
print(c.most_common(3))
print(list(c))
