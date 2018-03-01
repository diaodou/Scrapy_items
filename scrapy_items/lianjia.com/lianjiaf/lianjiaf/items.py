# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiafItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_url=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    type=scrapy.Field()
    price=scrapy.Field()

