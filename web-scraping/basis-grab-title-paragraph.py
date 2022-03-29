import requests

result = requests.get("http://www.example.com")
# print(type(result))
# print(result.text)

import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
print(soup.select('title'))
print(soup.select('title')[0].getText())
print('\n'*3)

print(soup.select('p'))
print(soup.select('p')[0].getText())
