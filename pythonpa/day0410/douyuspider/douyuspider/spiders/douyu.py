# -*- coding: utf-8 -*-
import scrapy
import json
from douyuspider.items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url]

    def parse(self, response):
        print('offset:', self.offset)
        data = json.loads(response.text)['data']

        for each in data:
            item =DouyuspiderItem()
            item['nickname'] = each['nickname']
            item['imageurl'] = each['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)













