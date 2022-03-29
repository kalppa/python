import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result.text,"lxml")

print('Grabe the Contents')
print(soup.select('.toctext'))
print(soup.select('.toctext')[0].text)

for item in soup.select('.toctext'):
    print(item.text)
