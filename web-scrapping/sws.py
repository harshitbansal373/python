'''import scrapy
from scrapy.crawler import CrawlerProcess
class Spiderclassname(scrapy.Spider):
    name="spider_name"
    
    def start_requests(self):
        urls=["https://www.datacamp.com/courses/all"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        links=response.css('div.course-block>a::attr(href)').extract()
        file_name='dc_links.csv'
        with open(file_name,'w') as f:
            f.writelines([link+'\n' for link in links])
    
process=CrawlerProcess()
process.crawl(Spiderclassname)
process.start()'''

import scrapy
from scrapy.crawler import CrawlerProcess
class Spiderclassname(scrapy.Spider):
    name="spider_name"
    
    def start_requests(self):
        urls=["https://beatmash.ml/"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        links=response.css('a::attr(href)').extract()
        file_name='dc_links.csv'
        with open(file_name,'w') as f:
            f.writelines([link+'\n' for link in links])
    
process=CrawlerProcess()
process.crawl(Spiderclassname)
process.start()
