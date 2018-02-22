from scrapy.contrib.spiders import SitemapSpider


class MySpider(SitemapSpider):
    def parse(self, response):
        pass

    sitemap_URLss = ['http://www.example.com/sitemap.xml']
    sitemap_rules = [('/electronics/', 'parse_electronics'), ('/apparel/', 'parse_apparel')]

    def parse_electronics(self, response):
        return None

    def parse_apparel(self, response):
        return None