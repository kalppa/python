"""
Concatenation
"""

name = 'cat'
first_letter = name[0]
last_letter = name[1:]
print(first_letter)
print(last_letter)

changed_first_letter = 'f'
print(changed_first_letter + last_letter)

def myfunc(word):
    string = ''
    for letter in word:
        string += letter*3
    return string

print(myfunc('word'))

def palindrome(s):
    # REMOVE SPACES STRING
    s = s.replace(' ','')
    # Check string is == reversed version of the string
    if s == s[::-1]:
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')
palindrome('nurses run')
