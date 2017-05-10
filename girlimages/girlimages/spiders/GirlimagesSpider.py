# -*- coding: utf8 -*-
# GFKARI CARD CRAWLER
# Version 1.0 - crawls images from gfkari.gamedbs.jp
# Part of the GFKARIDATABASE project.

import scrapy
import json
import math
import hashlib
import datetime
from girlimages.items import GirlimagesItem

class GirlimagesSpider(scrapy.Spider):
    name = 'girlimages'
    start_urls = []
    def __init__(self):
        for i in range(220):
            self.start_urls.append("http://gfkari.gamedbs.jp/girl/detail/" + str(1 + i))

    def parse(self, response):
        urls = response.xpath("//section//a[contains(@data-lightbox, 'profile-set')]/img/@src").extract()
        for i in range(len(urls)):
            item = GirlimagesItem()
            url = 'http://gfkari.gamedbs.jp' + urls[i]
            request = scrapy.Request(url=url, callback=self.image_parser)
            start = url.find("profile_") + 8
            end = url.find(".png")
            girl_id = url[start:end]
            girl_id.lstrip()
            item['image_url'] = url
            request.meta['girl_id'] = girl_id
            request.meta['item'] = item
            yield request

    def image_parser(self, response):
        item = response.meta['item']
        girl_id = response.meta['girl_id']
        # hash generation so people don't crawl my database
        # im salty that nobody has a easy-to-crawl db ok
        m = hashlib.md5()
        m.update(str(datetime.datetime.now()))
        image_name = m.hexdigest()
        item['girl_id'] = girl_id
        item['image_name'] = image_name
        yield item
