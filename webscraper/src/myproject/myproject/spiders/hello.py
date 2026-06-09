import scrapy


class QuotesSpider(scrapy.Spider):
    name = "hello"
    
    def parse(self, response):
        self.log("Hello, world! This is my first Scrapy spider.")   