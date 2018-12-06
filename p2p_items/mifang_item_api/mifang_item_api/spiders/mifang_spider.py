# -*- coding: utf-8 -*-
import scrapy
import time


class MifangSpiderSpider(scrapy.Spider):
    name = 'mifang_spider'
    #allowed_domains = ['www.mifang.com']
    #start_urls = ['http://www.mifang.com/']
    def start_requests(self,page=0):
        while True:
            page+=1
            url = 'http://118.178.192.232/sift/siftRecord'
            data = 'isGroup=&isHot=&isDistrict=&pageNum={page}&pointWord=&address=%E6%B8%A9%E5%B7%9E&district=-1&district_id=0&minArea=0&maxArea=0&minPrice=0&maxPrice=0&minAll=0&maxAll=0&handTime=-1'.format(page=page)
            yield [scrapy.FormRequest(url=url,formdata=data,callback=self.parse)]
            time.sleep(3)
    def parse(self, response):
        print(response.text)

