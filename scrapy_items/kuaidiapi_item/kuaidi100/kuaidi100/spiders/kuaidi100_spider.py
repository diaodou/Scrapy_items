# -*- coding: utf-8 -*-
import pdb

from scrapy import Spider,Request,FormRequest
from kuaidi100.ExpressCompany import CompanyName
from kuaidi100.items import Kuaidi100Item
'''
    70024024991235 70024024991235	百世汇通（百世快递)	huitongkuaidi
	70108338381532  百世汇通（百世快递）  huitongkuaidi
    1.实现
        1.代码与快递公司的转换
        2.useragent池子
        3.多进程(multiprocessing)

'''

class Kuaidi100SpiderSpider(Spider):
    name = 'kuaidi100_spider'
    allowed_domains = ['www.kuaidi100.com']
    #start_urls = ['http://www.kuaidi100.com/']
    methad = 'get'
    NU = input('请输入快递单号:')
    COM = input('快递名:')


    #构建请求
    def start_requests(self):
        if self.methad == 'get':
            companyname = CompanyName()
            COMS = companyname.parse_com(self.COM)  #返回对应代码
            url = 'http://api.kuaidi100.com/api?id=94eb250be18600db&com={COM}&nu={NU}&show=0&muti=1&order=desc'.format(NU=self.NU,COM=COMS)
            yield Request(url,callback=self.parse_response)
        elif self.methad == 'post':
            url = 'http://api.kuaidi100.com/api?id=94eb250be18600db&com={COM}&nu={NU}&show=0&muti=1&order=desc'.format(NU=self.NU,COM=self.COM)
            yield FormRequest(url,callback=self.parse_response)

    #解析json
    def parse_response(self,response):
        item = Kuaidi100Item()
        if response.status ==200:
            if isinstance(response.text,str) == True:
                result_dict = eval(response.text)
                parse_result = result_dict.get('data')
                company = result_dict.get('com')
                companyname = CompanyName()
                companys = companyname.descarn_company(company)     #将公司代码转换成中文

                print('快递公司:{}'.format(companys))
                print('快递单号:{}'.format(self.NU))
                for  s in parse_result:
                    start_data = s.get('context','N\A')
                    data = s.get('time')+','+start_data
                    print(data)


