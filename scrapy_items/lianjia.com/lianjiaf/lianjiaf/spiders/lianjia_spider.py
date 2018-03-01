# -*- coding: utf-8 -*-
import re

from scrapy import Spider
from bs4 import BeautifulSoup
from lianjiaf.items import LianjiafItem
from scrapy.spider import CrawlSpider,Rule,Request
from scrapy.linkextractors import LinkExtractor
import os


class LianjiaSpiderSpider(Spider):
    name = 'lianjia_spider'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']
    def parse(self, response):
        item = LianjiafItem()
        data = BeautifulSoup(response.text,'lxml').find_all('li',class_='clear')
        for tag in data:
            page_url = response.url
            title = tag.find('div',class_='title').get_text()
            url = tag.div.find('a',attrs={'data-el':'ershoufang'})['href']
            type = tag.find('div',class_='houseInfo').get_text()
            price = tag.find('div',class_='totalPrice').get_text().replace('万','')
            for field in item.fields:
                item[field] = eval(field)
            yield item
        page = response.xpath('//div[@comp-module="page"]').re('lPage\"\:(\d+)')[0]
        for u in range(1,int(page)+1):
            urls = 'https://bj.lianjia.com/ershoufang/pg{}'.format(u)
            yield Request(urls,callback=self.parse)


















