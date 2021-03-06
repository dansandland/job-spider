from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor


class JobSpider(Spider):
    name = 'jobspider'

    def __init__(self, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        self.le = LinkExtractor()

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        for url in response.meta['redirect_urls']:
            logging.info('response.meta[redirect_urls]: %s' % url)        

        # for link in self.le.extract_links(response):
        #     r = Request(url=link.url)
        #     r.meta.update(link_text=link.text)
        #     yield r

