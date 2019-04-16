# -*- coding: utf-8 -*-
import scrapy
from homeWork.items import HomeworkItem

class Sun1Spider(scrapy.Spider):
    name = 'sun1'
    allowed_domains = ['wz.sun0769.com']
    url = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    offter = 0
    start_urls = [url]

    def parse(self, response):
        lj = response.xpath('//a[@class="red14"]/@href').extract()
        print('len:', len(lj))
        for l in lj:
            yield scrapy.Request(l, callback=self.parse_item)

        if self.offter < 30000:
            self.offter += 30
            yield scrapy.Request(self.url+str(self.offter), callback=self.parse)

    def parse_item(self,response):
        item = HomeworkItem()
        # 标题
        item['name'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        # 编号
        item['number'] = \
        response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].strip().split(':')[-1]
        # 编号
        item['url'] = response.url
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()

        tmp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip().split(' ')
        item['author'] = tmp[0].split('：')[-1]
        item['pub_date'] = tmp[1].split('：')[-1] + ' ' + tmp[2]

        yield item