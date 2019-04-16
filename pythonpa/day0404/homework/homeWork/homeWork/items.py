# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 1、阳光热线问政平台爬虫（CrawlSpider）
    # http://wz.sun0769.com/index.php/question/questionType?type=4&page=
    # 爬去投诉帖子的标题，编号，链接，内容，投诉者，投诉时间
    # 存储到mysql数据库

    name = scrapy.Field()
    number = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pub_date = scrapy.Field()

