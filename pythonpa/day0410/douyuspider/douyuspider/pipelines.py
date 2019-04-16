# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class DouyuspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imageurl = item['imageurl']
        yield scrapy.Request(imageurl)


    # def item_completed(self, results, item, info):