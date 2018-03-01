import json

import scrapy
import pdb
from zhihua.items import ZhihuaItem
from scrapy.shell import inspect_response
import logging

class ZhihuSPider(scrapy.Spider):

    logging = logging.getLogger(__name__)
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls   = ['http://www.zhihu.com']
    #user = 'https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
    #follow = 'https://www.zhihu.com/api/v4/members/shi-tou-87-54?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    start_user = 'excited-vczh'


    #user_url是个人信息
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_include = 'allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    # follow_url是粉丝列表
    follow_url = 'https://www.zhihu.com/api/v4/members/{user}/{include}offset={offset}&limit={limit}'
    follow_include = 'followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?{include}offset={offset}&limit={limit}'
    followers_include='data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&'
    #https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20

    def start_requests(self):

        yield scrapy.Request(self.user_url.format(user=self.start_user,include=self.user_include),callback=self.parse_user)
        #^将个人信息放入parse_user函数中解析

        yield scrapy.Request(self.follow_url.format(user=self.start_user,include=self.follow_include,offset=0,limit=20),callback=self.parse_follow)
        #yield scrapy.Request(self.followers_url.format(user=self.start_user,include=self.followers_include,offset=0,limit=20),callback=self.parse_followers)
        #pdb.set_trace() #debug调试
    #解析个人信息
    def parse_user(self,response):
        #self.logger.debut('logging____________________________________!')
        item = ZhihuaItem()

        #inspect_response(response,self)
        user_data =json.loads(response.text)
        for field in item.fields:
            if field in user_data.keys():
                item[field] = user_data.get(field)
        yield item         #记得return 到item才能导出数据
        yield scrapy.Request(self.follow_url.format(user=user_data.get('url_token'),include=self.follow_include,offset=0,limit=20),callback=self.parse_follow)

    #解析粉丝信息
    def parse_follow(self,response):
        follow_data = json.loads(response.text)
        if 'data' in follow_data.keys():
            for data in follow_data.get('data'):

                yield scrapy.Request(self.user_url.format(user=data['url_token'],include=self.user_include),callback=self.parse_user)
                #^把start_user的粉丝解析后，的response传递给parse_user,获得个人信息
                yield scrapy.Request(self.follow_url.format(user=data['url_token'],include=self.follow_include,offset=0,limit=20),callback=self.parse_follow)
                #^把start_user的粉丝解析后，将粉丝的粉丝信息调用给parse_follow解析，获得粉丝的粉丝信息
        #
        # if 'paging' in follow_data.keys() and follow_data.get('paging').get('is_end') ==False:
        #     next_page = follow_data.get('paging').get('next')
        #     pdb.set_trace()
        #     yield scrapy.Request(url=next_page,callback=self.parse_follow)
        #     #判断下一页回调给自己

    # def parse_followers(self, response):
    #     follow_data = json.loads(response.text)
    #     if 'data' in follow_data.keys():
    #         for data in follow_data.get('data'):
    #             yield scrapy.Request(self.user_url.format(user=data['url_token'], include=self.user_include),
    #                                  callback=self.parse_user)
    #             # ^把start_user的粉丝解析后，的response传递给parse_user,获得个人信息
    #             yield scrapy.Request(
    #                 self.follow_url.format(user=data['url_token'], include=self.followers_include, offset=0, limit=20),
    #                 callback=self.parse_followers)
    #             # ^把start_user的粉丝解析后，将粉丝的粉丝信息调用给parse_follow解析，获得粉丝的粉丝信息
    #     if 'paging' in follow_data.keys() and follow_data.get('paging').get('is_end') == False:
    #         next_page = follow_data.get('paging').get('next')
    #         yield scrapy.Request(next_page, callback=self.parse_followers)











