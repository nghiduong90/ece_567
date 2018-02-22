from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.item import Item, Field


class NewsItem(Item):
    title = Field()
    link = Field()
    desc = Field()


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.google.com']
    start_urls = ['https://news.google.com']

    rules = (

        Rule(LinkExtractor(allow='cnn.com', deny='http://edition.cnn.com/')),
        Rule(LinkExtractor(allow=('news.google.com', )), callback='parse_news_item'))

    def parse_news_item(self, response):
        sel = Selector(response)
        item = NewsItem()
        item['title'] = sel.xpath('//title/text()').extract()
        item['topic'] = sel.xpath('/div[@class="topic"]').extract()
        item['desc'] = sel.xpath('//td//text()').extract()
        return sel
