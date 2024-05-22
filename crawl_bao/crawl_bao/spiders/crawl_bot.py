import scrapy
from ..items import CrawlBaoItem
from scrapy_selenium import SeleniumRequest
from scrapy_splash import SplashRequest
class CrawlBotSpider(scrapy.Spider):
    name = "crawl_bao"
    #allowed_domains=['https://dantri.com.vn/']
    start_urls = [
        "https://dantri.com.vn/"
                  ]
#     script='''
# function main(splash, args)
#   assert(splash:go(args.url))
#   assert(splash:wait(0.5))
#   return {
#     html = splash:html(),
#     png = splash:png(),
#     har = splash:har(),
#   }
# end
#     '''
    
    def start_requests(self):
        #url='https://dantri.com.vn/'
        #yield SplashRequest(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'},callback=self.parse)
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

    def parse(self, response):
        product= CrawlBaoItem()
        name=response.css('a.dt-text-black-mine::attr(href)').getall()
        self.logger.info(f'Extracted heading: {name}') 
        product["name"]=name
        yield product
