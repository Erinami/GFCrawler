# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GirlsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    girl_id = scrapy.Field()
    name = scrapy.Field()
    name_hiragana = scrapy.Field()
    name_eng = scrapy.Field()
    cv = scrapy.Field()
    cv_eng = scrapy.Field()
    age = scrapy.Field()
    birthday = scrapy.Field()
    blood = scrapy.Field()
    bust = scrapy.Field()
    school = scrapy.Field()
    school_eng = scrapy.Field()
    className = scrapy.Field()
    year = scrapy.Field()
    club = scrapy.Field()
    club_eng = scrapy.Field()
    description = scrapy.Field()
    description_eng = scrapy.Field()
    favorite_food = scrapy.Field()
    favorite_food_eng = scrapy.Field()
    hated_food = scrapy.Field()
    hated_food_eng = scrapy.Field()
    favorite_subject = scrapy.Field()
    favorite_subject_eng = scrapy.Field()
    height = scrapy.Field()
    hip = scrapy.Field()
    hobby = scrapy.Field()
    hobby_eng = scrapy.Field()
    nickname = scrapy.Field()
    nickname_eng = scrapy.Field()
    horoscope = scrapy.Field()
    horoscope_eng = scrapy.Field()
    tweetName = scrapy.Field()
    waist = scrapy.Field()
    weight = scrapy.Field()
    girlType = scrapy.Field()
    authority = scrapy.Field()
    translated = scrapy.Field()
    priority = scrapy.Field()
