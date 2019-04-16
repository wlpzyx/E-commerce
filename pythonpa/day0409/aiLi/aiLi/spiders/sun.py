# -*- coding: utf-8 -*-
import scrapy


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['http://tejia.aili.com/index_5.html']
    start_urls = ['http://http://tejia.aili.com/index_5.html/']

    def parse(self, response):
        pass
