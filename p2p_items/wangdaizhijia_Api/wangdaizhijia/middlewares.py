# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import time

import requests
from scrapy import signals
#from wangdaizhijia.settings import IPPOOL

from wangdaizhijia.RandomUserAgentMiddleware import RandomUserAgentMiddleware

''''  
    1.实现代理替换2个方法
    
    2.尝试当无代理可用的时候执行：
        from scrapy import cmdline
        if response.start_code != 200:
            cmdline.execute('scrapy genspider proxy.py').split()

'''

import base64

# 代理服务器
proxyServer = "http://http-pro.abuyun.com:9010"

# 代理隧道验证信息
proxyUser = "H01234567890123P"
proxyPass = "0123456789012345"


class WangdaizhijiaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.




#3      使用付费代理接口
###########################################################################################
    # for Python2
    # proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
    #
    # for Python3


    # proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
    # def process_request(self, request, spider):
    #     request.meta["proxy"] = proxyServer
    #     request.headers["Proxy-Authorization"] = self.proxyAuth
    #     print('目前使用的代理:%s'%request.meta['proxy'])
    #     print('目前使用的请求头:%s'%request.headers['Proxy-Authorization'])

#1
###########################################################################

    '''这里实现了修改代理， 从setting中取出可用的代理'''
    # def __init__(self,ip=''):
    #     self.ip = ip
    # def process_request(self,request,spider):
    #     thisip =random.choice(IPPOOL)                       #random.choice随机ip代理
    #     print('this is ip :'+thisip['ipaddr'])              #打印测试
    #     request.meta['proxy'] = 'http://'+thisip['ipaddr']  #setting文件里面的key

#2
####################################################################
    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        print("this is request ip:" + proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('c://data//proxies_p2p.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        print(proxy)
        # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        # response = requests.get(url = 'https://shuju.wdzj.com/',headers = headers,proxies=proxy)
        # if response.status_code == 200:
        #     print(response.text)

        print('目前使用的代理:%s'%proxy)
        return proxy


        # 因为这里没有使用验证，我使用request验证一下这个代理再返回

    ##########################################################################
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WangdaizhijiaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
    '''设置response'''
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest



        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
