# BOOKS_TO_SCRAPE

This repository contains two spiders that scrape data from the "http://books.toscrape.com" website and save it to a MongoDB database. Each spider is located in its respective folder.

## Folder: `books_lv`

This folder contains a spider named `BooksToscrapeSpider` that scrapes book information from the "Mystery" category on the website. The spider starts with the URL "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html" and follows the pagination to scrape multiple pages.

### Spider Details

- **Spider Name**: `books_lv`
- **Start URL**: "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"

#### Spider Fields Scraped

The spider extracts the following fields for each book:

- `book_name`: The name of the book.
- `book_price`: The price of the book.
- `book_ratings`: The rating of the book.
- `book_url`: The URL of the book.

### Dependencies

- `scrapy`: The Scrapy framework is used for web scraping.
- `pymongo`: The PyMongo library is used to interact with the MongoDB database.

## Folder: `books_pv`

This folder contains a spider named `BooksToscrapeSpider` that retrieves book details from the MongoDB database and then scrapes additional information for each book.

### Spider Details

- **Spider Name**: `books_pv`
- **Start URLs**: Retrieved from the MongoDB database

#### Spider Fields Scraped

The spider extracts the following fields for each book:

- `book_description`: The description of the book.
- `upc`: The Universal Product Code (UPC) of the book.
- `book_imageurl`: The URL of the book's image.
- `availability`: The availability status of the book.

### Dependencies

- `scrapy`: The Scrapy framework is used for web scraping.
- `pymongo`: The PyMongo library is used to interact with the MongoDB database.

## MongoDB Integration

Both spiders interact with a MongoDB database to store and retrieve book information. The connection to the MongoDB server is established using the following configuration:

- **Host**: localhost
- **Port**: 27017
- **Database**: booksdb
- **Collection**: mystery_books

The `books_lv` spider inserts each book's information as a new document into the `mystery_books` collection. The `books_pv` spider retrieves the book URLs from the `mystery_books` collection and updates the existing documents with additional information.

To run these spiders, ensure that you have MongoDB installed and running on your local machine.

## Running the Spiders

To run the spiders, follow these steps:

1. Install the required dependencies (`scrapy` and `pymongo`).
2. Open a terminal or command prompt.
3. Navigate to the respective spider's folder (`books_lv` or `books_pv`).
4. Execute the following command to start the spider:

   ```bash
   scrapy crawl <spider_name>
   ```

   Replace `<spider_name>` with the name of the spider you want to run (`books_lv` or `books_pv`).

   Example command to run the `books_lv` spider:

   ```bash
   scrapy crawl books_lv
   ```

   Example command to run the `books_pv` spider:

   ```bash
   scrapy crawl books_pv
   ```

The spiders will scrape the book data and store it in the MongoDB database according to their respective functionalities.

Please note that running the `books_lv` spider first is necessary to populate the database before using the `books_pv` spider to retrieve additional information.# BooksToScrape
