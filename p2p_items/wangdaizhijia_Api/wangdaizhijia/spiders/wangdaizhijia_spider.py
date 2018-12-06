# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from scrapy.shell import inspect_response
from wangdaizhijia.items import WangdaizhijiaItem

from multiprocessing import Pool

'''实现emal提醒'''
from wangdaizhijia.smtp_email import SMTP_Email
'''
    实现
        1.邮件提醒
        2.ip代理更换


'''


class WangdaizhijiaSpiderSpider(Spider):
    name = 'wangdaizhijia_spider'
    #allowed_domains = ['https://shuju']
    start_urls = ['http://www.shuju/']


    def start_requests(self):
        pageone_url = 'https://shuju.wdzj.com/'
        yield Request(url = pageone_url,callback=self.parse_pageone)


    def parse_pageone(self,response):

        company_names =  response.xpath('//div[@class="td-wrap"]').re('html"\>(.*?)</a>')
        pageone_link = response.xpath('//div[@class="td-wrap"]/a/@href').re('(//shuju.*.html)')
        for link in pageone_link:
            links = 'https:{}'
            #print(links.format(link))
            yield Request(url=links.format(link),callback=self.parse_pagetwo)#,meta={'name':company_names})
    def parse_pagetwo(self,response):
        #name = response.meta['name']
        item =WangdaizhijiaItem()
        try:
            company_link = response.xpath('//div[@class="pt-link"]/a/@data-href').extract()[0].strip()
            company_name = response.xpath('//div[@class="title"]/h1/@alt').extract()[0].strip()
            # for field in item.fields:
            #     item[field] = eval(field)
            item['company_link'] = company_link
            item['company_name'] = company_name
            #print(item['company_name'],item['company_link'])
            print(item)
            yield item
        except Exception as e:
            print(e)
            # s = SMTP_Email()
            # s.main(subject='异常错误!', content='error is:' % e)  # 实现email提醒
            # raise RuntimeError('error!!')
            #from scrapy.shell import inspect_response
            #inspect_response(response,self)







