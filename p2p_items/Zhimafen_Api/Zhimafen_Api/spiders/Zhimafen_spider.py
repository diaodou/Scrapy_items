# -*- coding: utf-8 -*-
import json
import re
import requests
import scrapy
import requests
import random,time
from scrapy import Spider,Request,FormRequest
from scrapy.shell import inspect_response
from Zhimafen_Api.items import ZhimafenApiItem
import xlrd

import xlwt
from datetime import date, datetime


class ZhimafenSpiderSpider(Spider):
    name = 'Zhimafen_spider'
    #allowed_domains = ['www.baidu.com']
    start_url = 'http://api.qhweidai.com/api/topicture'
    def start_requests(self):
        workbook = xlrd.open_workbook(r'C:\\Users\\99329\\Desktop\\待测试数据.xls')


        for i in self.open_file():
            s = i.strip()
            #s = 'http://upload.51qianmai.com/20180126064925821.jpg'
            data = {'channel':'abc','picturl':s}
        #data = {'channel':'abc','picturl':i}
            yield FormRequest(url=self.start_url,formdata=data,callback=self.parse,meta={'url':s})

    


    def parse(self, response):
        try:
            url = response.meta.get('url')
            data_dict = json.loads(response.text)
            code = data_dict.get('code')
            try:
                if code ==200:
                    items = ZhimafenApiItem()
                    data = data_dict.get('data','N/A')
                    fen = str(data)
                    #zhima = re.findall('(zhima.*分)',fen)
                    zhima = data.get('zhima')
                    url = response.meta.get('url')
                    items['data'] = data_dict
                    items['zhima'] = zhima
                    items['url'] = url
                    return items
                if code == 400:
                    print('error ！！！')
                    self.save_file(url)
            except Exception as e:
                print(e)


                # print(data_dict)
                # zhima = re.findall('(zhima.*分)',str(response.text))     #芝麻分
                #url = response.meta.get('url')
                #
                # items['zhima'] = str(zhima)
                # items['code_200'] = url
        except Exception as e:
            print(e)
    def save_file(self,url):
        with open('C:\\Users\\99329\\Desktop\\error17.txt', 'a') as f:
            f.write(url + '\n')
            print('成功写入！')
    def open_file(self):
        with open('C:\\Users\\99329\\Desktop\\5.txt', 'r') as f:
            origin = f.readlines()
            return origin

    def open_files(self):
        with open('C:\\Users\\99329\\Desktop\\parse_json.txt', 'r') as f:
            origin = f.readlines()
            return origin
