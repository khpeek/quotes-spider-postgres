import scrapy
from quotescraper.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
#    custom_settings = {'CLOSESPIDER_ERRORCOUNT': '1'}

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('span small::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item

#        next_page = response.css('li.next a::attr(href)').extract_first()
#        if next_page is not None:
#            yield response.follow(next_page, callback=self.parse)