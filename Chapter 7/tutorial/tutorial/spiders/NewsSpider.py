from scrapy.spiders import Spider


class NewsSpider(Spider):
    name = "news"
    allowed_domains = ["nytimes.com"]
    start_URLss = [
        'http://www.nytimes.com/'
    ]

    def parse(self, response):
        filename = response.URLs.split("/")[-2]
        open(filename, 'wb').write(response.body)
