from lxml import html
import requests

response = requests.get('https://books.toscrape.com/')
books = html.fromstring(response.content)
book_elements = books.xpath('//article[@class="product_pod"]')

Stars = {
   "One" : '★ ☆ ☆ ☆ ☆',
   "Two" : '★ ★ ☆ ☆ ☆',
   "Three" : '★ ★ ★ ☆ ☆',
   "Four" : '★ ★ ★ ★ ☆',
   "Five" : '★ ★ ★ ★ ★'
}

index = 0
for book in book_elements:
   title = book.xpath('//h3//a/@title')[index] 

   rating = book.xpath('//p[contains(@class, "star-rating")]/@class')[index]
   rating = rating.split()[-1]
   rating = Stars.get(rating)

   price = book.xpath('//p[contains(@class, "price_color")]/text()')[index]
   print(f"Book-Title: {title}\nStar-Rating: {rating}\nPrice: {price}\n")
   index+=1