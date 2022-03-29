import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(result.text,"lxml")

print('Grab the Image')

# Grab all the images
# print(soup.select('img'))

# Grab only the images in the main article
print(soup.select('.image'))
print(soup.select('.image')[0])
print(soup.select('.image')[0].next_element['src'])

computer = soup.select('.image')[0].next_element['src']
print(computer)

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('my_image.jpg','wb')
f.write(image_link.content)
f.close()