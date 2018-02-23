# -*- coding: utf-8 -*-
import scrapy


class KuaidiniaoSpiderSpider(scrapy.Spider):
    name = 'kuaidiniao_spider'
    allowed_domains = ['www.kdniao.com']
    start_urls = ['http://www.kdniao.com/']

    def parse(self, response):
        pass
