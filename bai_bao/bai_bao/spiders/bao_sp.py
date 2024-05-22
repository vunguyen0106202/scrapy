import scrapy
from ..items import BaiBaoItem
import csv


class BaoSpSpider(scrapy.Spider):
    name = "bao_sp"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]
    def start_requests(self):
        csv_file = 'linkssp.csv'
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                links = row[0].split(',')
                for link in links:
                    url=link.strip()            
                    #url="https://spiderum.com/bai-dang/4-thang-17M-tim-200k-follows-Bai-hoc-xay-tiktok-cua-minh-Phan-2-T80IGqWqa5y7"
                    yield scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
    def parse(self, response):
        product = BaiBaoItem()
        title = response.css('div.auth-container h1.ng-star-inserted::text').get()
        #product["name"] = title.strip() if title else None
        title1 = response.css('div.auth-container p.break-words::text').get()
        #product["name"] = title1.strip() if title1 else None
        paragraphs = response.css('div.ce-paragraph::text').extract()
        if not paragraphs:
            paragraphs = response.css('div.text-align::text').extract()

        content_text = ' '.join(paragraphs)

        #self.logger.info(f'Extracted content: {content_text}') 
        product["name"] = content_text.strip() if content_text else None
        yield product
