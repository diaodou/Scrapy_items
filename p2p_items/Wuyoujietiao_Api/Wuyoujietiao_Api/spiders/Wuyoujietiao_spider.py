# -*- coding: utf-8 -*-
import scrapy


class WuyoujietiaoSpiderSpider(scrapy.Spider):
    name = 'Wuyoujietiao_spider'
    allowed_domains = ['www.wuyoujietiao.com']
    start_urls = ['http://www.wuyoujietiao.com/']

    def parse(self, response):
        pass
