text = "The agent's phone number is 408-555-1234. Call soon!"

import re

pattern = 'phone'
match = re.search(pattern,text)
match.span()

text = 'My phone number is 408-555-1234'
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
# phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
#
# print(phone)
# print(phone.group())

"""Group Expressions"""
phone = re.search(r'(\d{3})-(\d{3})-(\d{4})',text)
print(phone)
print(phone.group())
print(phone.group(3))
