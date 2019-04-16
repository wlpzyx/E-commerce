# -*- coding: utf-8 -*-
import scrapy


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html']

    def parse(self, response):
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        item = JobspiderItem()
        items = []
        for each in job_list:
            name =each.xpath('normalize-space(./p/span/a/text())').extract()[0]
            city = each.xpath('./span[@class="t3"]/text()').extract()[0]
            pub_date = each.xpath('.//span[@class="t5"]/text()').extract()[0]
            salary = each.xpath('.//span[@class="t4"]/text()').extract()

















