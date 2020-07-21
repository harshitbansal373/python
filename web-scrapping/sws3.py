import scrapy
from scrapy.crawler import CrawlerProcess
class Spiderclassname(scrapy.Spider):
    name="spider_name"
    
    def start_requests(self):
        urls=["https://www.datacamp.com/courses/all"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        links=response.css('div.course-block>a::attr(href)').extract()
        for link in links:
          yield response.follow(url=link,callback=self.parse2)
            
    def parse2(self,response):
        crs_title=response.xpath('//h1[contains(@class,"title")]/text()').extract_first().strip()
        ch_titles=[t.strip() for t in response.css('h4.chapter__title::text').extract()]
        dc_dict=dict()
        dc_dict[crs_title]=ch_titles
        file_name='t.csv'
        with open(file_name,'a') as f:
            f.writelines('*****'+crs_title+'*****\n')
            f.writelines(t+'\n' for t in dc_dict[crs_title])

process=CrawlerProcess()
process.crawl(Spiderclassname)
process.start()
