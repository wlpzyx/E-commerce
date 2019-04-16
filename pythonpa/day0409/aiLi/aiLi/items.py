# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # http://tejia.aili.com/index.html
    # 爬取20页，提取商品名称，url，价格
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()

