#how to user

# fast item.py setting
# class AppleItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     title = scrapy.Field()
#     content = scrapy.Field()
#     time = scrapy.Field()
#     #pass
#scrapy crawl apple -o apple.json -t json
import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem
#from scrapy.spider import CrawlSpider
#from scrapy.linkextractors import LinkExtractor
class AppleCrawle(scrapy.Spider):
    name = 'apple'
    start_urls = ['https://bbs.hupu.com/']
    def parse(self, response):
        domain = 'https://bbs.hupu.com/'
        res = BeautifulSoup(response.text,'lxml')
        for news in res.select('.textSpan'):
            #print(news.select('span')[0].text)
            #print(domain + news.select('a')[0]['href'])
            yield scrapy.Request(domain + news.select('a')[0]['href'],self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.text,'lxml')
        appleitem = AppleItem()
        appleitem['title'] = res.select('h1')[0].text
        appleitem['content'] =res.select('.case')[0].text 
        appleitem['time'] = res.select('.stime')[0].text
        #print (res.select('h1')[0].text)
        return appleitem
