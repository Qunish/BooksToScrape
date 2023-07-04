# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksToscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_ratings = scrapy.Field()
    book_url = scrapy.Field()
    pass

class BooksToscrapeItem_pv(scrapy.Item):
    book_description = scrapy.Field()
    upc = scrapy.Field()
    availability = scrapy.Field()
    book_imageurl = scrapy.Field()
    pass