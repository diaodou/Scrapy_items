# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item
import scrapy

class LianjiaaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host_type= scrapy.Field()
    host_price = scrapy.Field()
    host_link = scrapy.Field()
    host_url = scrapy.Field()
