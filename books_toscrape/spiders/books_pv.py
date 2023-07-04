import scrapy
from ..items import BooksToscrapeItem_pv
import pymongo
from urllib.parse import urljoin

class BooksToscrapeSpider(scrapy.Spider):
    name = "books_pv"

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["booksdb"]
        self.collection = db["mystery_books"]

        self.start_urls = [document['book_url'] for document in self.collection.find()]

    def parse(self, response):
            items = BooksToscrapeItem_pv()
            book_description = response.css("#product_description+ p::text").extract_first()
            upc = response.css("tr:nth-child(1) td::text").extract_first()
            availability = response.css("tr:nth-child(6) td::text").extract_first()

            base_url = 'http://books.toscrape.com/'
            relative_url = response.css(".thumbnail img::attr(src)").extract_first()
            book_imageurl = urljoin(base_url, relative_url)


            items['book_description'] = book_description
            items['upc'] = upc
            items['book_imageurl'] = book_imageurl
            items['availability'] = availability

            self.collection.update_one(
                {'book_url': response.url},
                {'$set': dict(items)},
                upsert=True
            )
            yield items
            
