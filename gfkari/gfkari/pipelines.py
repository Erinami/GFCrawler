# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

class GfkariPipeline(object):
    def process_item(self, item, spider):
        return item

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
    self.exporter.fields_to_export = ['card_id','girl_id','set_type','set_id','set_name_initial', 'set_name_initial_eng', 'set_name_final','set_name_final_eng', 'set_position','set_rarity',
    'card_stat_display','set_size','attribute','cost','description','description_eng','disposal','before_evolution_uid','evolution_uid',
    'max_level','initial_level','skill_name','skill_name_eng','name','name_eng','rarity','strongest_level','skill_description','skill_description_eng','initial_attack_base','initial_defense_base',
    'max_attack_base','max_defense_base','information_missing','translation_status', 'stat_status','flagged']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    item.setdefault('translation_status', 0)
    item.setdefault('stat_status', 0)
    item.setdefault('set_type', 'normal')
    item.setdefault('information_missing', 0)
    self.exporter.export_item(item)
    return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class CardImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        links = [item['image_url'], item['thumbnail']]
        yield scrapy.Request(links[1], meta={'image_name': item["card_id"], 'thumbnail':'true'})
        # yield scrapy.Request(link[0], meta={'image_name': item["card_id"], 'thumbnail':'false'})
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)

   # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        for key, image, buf, in super(CardImagesPipeline, self).get_images(response, request, info):
            key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        if response.meta['thumbnail'] == "true":
            return "thumbnail_card_" + response.meta['image_name'] + ".jpg"
        else:
            return "card_" + response.meta['image_name'] + ".jpg"
