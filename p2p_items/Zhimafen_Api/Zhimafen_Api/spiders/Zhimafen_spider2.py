



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
    name = 'Zhimafen_spider2'
    #allowed_domains = ['www.baidu.com']
    start_url = 'http://api.qhweidai.com/api/topicture'

    def __init__(self):
        pass

    def start_requests(self):
        workbook = xlrd.open_workbook(r'C:\\Users\\99329\\Desktop\\待测试数据.xls')
        # 根据sheet索引或者名称获取sheet内容
        sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
        i = 0
        try:
            # while True:
            #     # 获取整行和整列的值（数组）
            #     i += 1
            #     rows = sheet2.row_values(i)  # 获取第四行内容
            #     # cols = sheet2.col_values(2)  # 获取第三列内容
            #     rows2 = rows[2]
            #     rows3 = rows[3]
                rows2 = 'http://upload.yueguangbaika.com/20171230024117923.jpg'
                rows3 = 'http://upload.yueguangbaika.com/20171230024239548.jpg'
                data2 = {'channel':'abc','picturl':rows2}
                data3 = {'channel':'abc','picturl':rows3}
                yield FormRequest(url=self.start_url,formdata=data2,callback=self.parse_response2,meta={'url2':rows2})
                yield FormRequest(url=self.start_url,formdata=data3,callback=self.parse_response3,meta={'url3':rows3})
        except Exception as e:
            print(e)

    '''parse有分数的'''
    def parse_response2(self, response):
        try:
            url = response.meta.get('url2')          #post的url
            data_dict = json.loads(response.text)
            code = data_dict.get('code')
            try:
                if code ==200:
                    items = ZhimafenApiItem()
                    data = data_dict.get('data','N/A')
                    zhima = data.get('zhima')
                    url = response.meta.get('url')
                    items['data'] = data_dict
                    items['zhima'] = zhima
                    items['url'] = url
                    return items
                if code == 400:
                    print('error ！！！')
                    return None
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


    '''parse违约的'''
    def parse_response3(self,response):
        items = ZhimafenApiItem()
        try:
            print('*3'*100)
            print(response.text)
            url = response.meta.get('url3')  # post的url
            data_dict = json.loads(response.text)
            code = data_dict.get('code')
            try:
                if code == 200:
                    items = ZhimafenApiItem()
                    data = data_dict.get('data', 'N/A')
                    zhima = data.get('zhima')
                    #url = response.meta.get('url3')
                    items['data'] = data_dict
                    items['zhima'] = zhima
                    items['url'] = url
                    return items
                elif code == 400:
                    content3 = {}
                    print('error ！！！')
                    js_3 = json.loads(response.text)
                    content3['uid'] = js_3.get('code')
                    #self.save_json()
                    return items
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)




    #保存为json
    def save_json(self,data):
        with open('../demo1.json','a')as f:
            js = json.dumps(data)
            f.write(js+'\n')
            print('写入完成！')

            
    def save_file(self,url):
        with open('C:\\Users\\99329\\Desktop\\error17.txt', 'a') as f:
            f.write(url + '\n')
            print('成功写入！')

    #打开问价
    def open_file(self):
        with open('C:\\Users\\99329\\Desktop\\5.txt', 'r') as f:
            origin = f.readlines()
            return origin

    def open_files(self):
        with open('C:\\Users\\99329\\Desktop\\parse_json.txt', 'r') as f:
            origin = f.readlines()
            return origin
