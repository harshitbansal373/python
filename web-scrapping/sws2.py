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
        for link in links:
          file_name='spider_links.csv'
          with open(file_name,'a') as f:
            f.writelines('====='+link+'=====\n')
          
          yield response.follow(url=link,callback=self.parse2)
            
    def parse2(self,response):
        links_title=response.xpath('/html/head/title/text()').extract_first().strip()
        links2=[t for t in response.css('a::attr(href)').extract()]
        file_name='spider_links.csv'
        with open(file_name,'a') as f:
            f.writelines('***'+links_title+'***\n')
            f.writelines(i+'\n' for i in links2)

process=CrawlerProcess()
process.crawl(Spiderclassname)
process.start()
