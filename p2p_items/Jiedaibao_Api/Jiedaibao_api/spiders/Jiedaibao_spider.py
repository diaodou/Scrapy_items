# -*- coding: utf-8 -*-
import scrapy


class JiedaibaoSpiderSpider(scrapy.Spider):
    name = 'Jiedaibao_spider'
    allowed_domains = ['www.jiedaibao.com']
    start_urls = ['http://www.jiedaibao.com/']

    def parse(self, response):
        pass
