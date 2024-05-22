import scrapy
from ..items import BaiBaoItem
import csv
class BaoSpider(scrapy.Spider):
    name = "bai_bao"
    #allowed_domains = ["dantri.com.vn"]
    #start_urls = ["https://dantri.com.vn/xa-hoi/gia-vang-bien-dong-phuc-tap-bo-cong-an-vao-cuoc-20240515101403243.htm"]

    def start_requests(self):
        csv_file = 'linkbaodantri.csv'
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                links = row[0].split(',')
        
                for link in links:
                    url="https://dantri.com.vn"+link.strip()
        #for url in self.start_urls:
                    yield scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

    
    
    def parse(self, response):
        product = BaiBaoItem()
        title = response.css('article.singular-container h1.title-page::text').get()
        #product["name"] = title.strip() if title else None
        title1 = response.css('article.singular-container h2.singular-sapo::text').get()
        #product["name"] = title.strip() if title1 else None

        paragraphs = response.css('div.singular-content > p::text').extract()
        content_text = ' '.join(paragraphs)

        #self.logger.info(f'Extracted content: {content_text}') 
        product["name"] = content_text.strip() if content_text else None
        yield product