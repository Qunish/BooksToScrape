import scrapy
from ..items import BooksToscrapeItem
import pymongo 
from urllib.parse import urljoin

class BooksToscrapeSpider(scrapy.Spider):
    name = "books_lv"
    start_urls = [
        "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"
    ]

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["booksdb"]
        self.collection = db["mystery_books"]

    def parse(self, response):
        items = BooksToscrapeItem()
        all_books = response.css(".product_pod")

        for book in all_books:
            book_name = book.css("h3 a::attr(title)").extract_first()
            
            base_url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
            relative_url = book.css("h3 a::attr(href)").extract_first()
            book_url = urljoin(base_url, relative_url)

            book_price = book.css(".price_color::text").extract_first()
            ratings = book.css('p.star-rating::attr(class)').get()
            rating_split = ratings.split()
            book_ratings = rating_split[-1]

            items["book_name"] = book_name
            items["book_price"] = book_price
            items["book_ratings"] = book_ratings
            items["book_url"] = book_url

            self.collection.insert_one(dict(items))
            yield items
    
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
        
