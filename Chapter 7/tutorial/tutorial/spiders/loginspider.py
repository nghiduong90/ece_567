from scrapy import FormRequest
from scrapy.spiders import BaseSpider
from scrapy import log


class LoginSpider(BaseSpider):
    name = 'example.com'
    start_URLss = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return [FormRequest.from_response(response,
                                          formdata={'username': 'john', 'password': 'secret'},
                                          callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
