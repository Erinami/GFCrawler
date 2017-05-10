# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class GfimagesPipeline(object):
    def process_item(self, item, spider):
        return item

class CardImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        link = item['image_url']
        yield scrapy.Request(link, meta={'image_name': item["image_name"], 'thumbnail':'false'})
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)

   # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        for key, image, buf, in super(CardImagesPipeline, self).get_images(response, request, info):
            key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return response.meta['image_name'] + ".jpg"

class CardThumbnailsPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        link = item['thumbnail_url']
        yield scrapy.Request(link, meta={'image_name': item["image_name"] + '-th', 'thumbnail':'false'})
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)

   # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        for key, image, buf, in super(CardThumbnailsPipeline, self).get_images(response, request, info):
            key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return response.meta['image_name'] + ".jpg"

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
    self.exporter.fields_to_export = ['card_id', 'image_name']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
