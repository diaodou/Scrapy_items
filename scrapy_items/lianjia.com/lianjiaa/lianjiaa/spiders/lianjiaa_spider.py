# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapy.linkextractor import LinkExtractor
from scrapy.spider import CrawlSpider,Rule
import scrapy
from lianjiaa.items import LianjiaaItem

class LianjiaaSpiderSpider(CrawlSpider):
    name = 'lianjiaa_spider'
    allowed_domains = ['www.lianjia.com']

    '''构造URL'''
    def start_requests(self):
        for page in range(1,100):
            start_urls = 'https://sz.lianjia.com/ershoufang/pg{}/'.format(page)
            yield scrapy.Request(url=start_urls,callback=self.parse)
    '''解析内容'''
    def parse(self, response):
        item = LianjiaaItem()
        soup = BeautifulSoup(response.text,'lxml').find_all('div',class_='info clear')
        for i in soup:
            item['host_type'] = i.find('div',class_='houseInfo').get_text()
            item['host_link'] = i.find('div',class_='houseInfo').find('a')['href']
            item['host_price'] = i.find('div',class_='priceInfo').find('div',class_='totalPrice').get_text().replace('万','')
            item['host_url'] = response.url
            yield item





