# -*- coding: utf-8 -*-
import scrapy


class ZhimafenOpenjpgSpider(scrapy.Spider):
    name = 'Zhimafen_openJpg'
    allowed_domains = ['www.zhima.com']
    start_urls = ['http://www.zhima.com/']

    def parse(self, response):
        pass






