# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    is_followed=scrapy.Field()
    avatar_url_template=scrapy.Field()
    user_type=scrapy.Field()
    answer_count=scrapy.Field()
    is_following=scrapy.Field()
    headline=scrapy.Field()
    url_token=scrapy.Field()
    id=scrapy.Field()
    allow_message=scrapy.Field()
    articles_count=scrapy.Field()
    is_blocking=scrapy.Field()
    type=scrapy.Field()
    name=scrapy.Field()
    url=scrapy.Field()
    gender=scrapy.Field()
    is_advertiser=scrapy.Field()
    avatar_url=scrapy.Field()
    is_org=scrapy.Field()
    follower_count=scrapy.Field()
    employments=scrapy.Field()
    badge=scrapy.Field()




















