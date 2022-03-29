""" Get title of every book with a 2-star rating """

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

result = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(result.text,'lxml')

# print(soup.select('.product_pod'))
products = soup.select('.product_pod')

# print(products[0])
# print(str(products[0]))

# print('\n'*3)
# print('-----Display how many books in one page -----')
# num_of_books = len(soup.select('.product_pod'))
# print(f' There are {num_of_books} books totally in this page.')

# print('star-rating Three' in str(products[0]))

example = products[0]
# print(example.select('.star-rating.Two'))
# print(example.select('a')[1]['title'])

two_star_titles = []

for n in range(1,3):
    scrape_url = base_url.format(n)
    result = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(result.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        # if 'star-rating Two' in str(book):
        if len(book.select('.start-rating.Two')) !=0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
