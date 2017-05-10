# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
import logging;
class GirlimagesPipeline(object):
    def process_item(self, item, spider):
        return item

class GirlImagesPipeline(FilesPipeline):

    globalItem = None

    def get_media_requests(self, item, info):
        link = item['image_url']
        self.globalItem = item
        yield scrapy.Request(link, meta={'image_name': item["image_name"], 'thumbnail':'false'})
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)

   # this is where the image is extracted from the HTTP response

    def file_key(self, url):
        start = url.find("profile_") + 8
        end = url.find(".png")
        return url[start:end] + ".png"

class CSVPipeline(object):


  def __init__(self):
    self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    self.exporter.fields_to_export = ['girl_id', 'image_name']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
