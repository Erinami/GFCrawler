# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GfkariItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    card_id = scrapy.Field()
    initial_attack_base = scrapy.Field()
    initial_defense_base = scrapy.Field()
    max_attack_base = scrapy.Field()
    max_defense_base = scrapy.Field()
    strongest_attack_base = scrapy.Field()
    strongest_defense_base = scrapy.Field()

    initial_attack_2MAX = scrapy.Field(default=0)
    initial_defense_2MAX = scrapy.Field(default=0)
    max_attack_2MAX = scrapy.Field(default=0)
    max_defense_2MAX = scrapy.Field(default=0)
    strongest_attack_2MAX = scrapy.Field(default=0)
    strongest_defense_2MAX = scrapy.Field(default=0)

    initial_attack_2STOCK = scrapy.Field(default=0)
    initial_defense_2STOCK = scrapy.Field(default=0)
    max_attack_2STOCK = scrapy.Field(default=0)
    max_defense_2STOCK = scrapy.Field(default=0)
    strongest_attack_2STOCK = scrapy.Field(default=0)
    strongest_defense_2STOCK = scrapy.Field(default=0)

    initial_attack_3MAX = scrapy.Field(default=0)
    initial_defense_3MAX = scrapy.Field(default=0)
    max_attack_3MAX = scrapy.Field(default=0)
    max_defense_3MAX = scrapy.Field(default=0)
    strongest_attack_3MAX = scrapy.Field(default=0)
    strongest_defense_3MAX = scrapy.Field(default=0)

    initial_attack_3STOCK = scrapy.Field(default=0)
    initial_defense_3STOCK = scrapy.Field(default=0)
    max_attack_3STOCK = scrapy.Field(default=0)
    max_defense_3STOCK = scrapy.Field(default=0)
    strongest_attack_3STOCK = scrapy.Field(default=0)
    strongest_defense_3STOCK = scrapy.Field(default=0)

    initial_attack_4MAX = scrapy.Field(default=0)
    initial_defense_4MAX = scrapy.Field(default=0)
    max_attack_4MAX = scrapy.Field(default=0)
    max_defense_4MAX = scrapy.Field(default=0)
    strongest_attack_4MAX = scrapy.Field(default=0)
    strongest_defense_4MAX = scrapy.Field(default=0)

    initial_attack_4STOCK = scrapy.Field(default=0)
    initial_defense_4STOCK = scrapy.Field(default=0)
    max_attack_4STOCK = scrapy.Field(default=0)
    max_defense_4STOCK = scrapy.Field(default=0)
    strongest_attack_4STOCK = scrapy.Field(default=0)
    strongest_defense_4STOCK = scrapy.Field(default=0)

    initial_attack_4STOCK = scrapy.Field()
    initial_defense_4STOCK = scrapy.Field()
    max_attack_4STOCK = scrapy.Field()
    max_defense_4STOCK = scrapy.Field()
    strongest_attack_4STOCK = scrapy.Field()
    strongest_defense_4STOCK = scrapy.Field()

    attribute = scrapy.Field()
    image_url = scrapy.Field()
    kana = scrapy.Field()
    cost = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    disposal = scrapy.Field()
    school_year = scrapy.Field()
    before_evolution_uid = scrapy.Field()
    thumbnail = scrapy.Field()
    evolution_uid = scrapy.Field()
    max_level = scrapy.Field()
    initial_level = scrapy.Field()
    skill_name = scrapy.Field()
    character_voice = scrapy.Field()
    name = scrapy.Field()
    rarity = scrapy.Field()
    strongest_level = scrapy.Field()
    skill_description = scrapy.Field()
    skill_description_eng = scrapy.Field()

    # the fields below are primarily used to construct the sets table. these fields will likely NOT be a part of the cards table, aside from set position
    set_id = scrapy.Field()
    set_name_initial = scrapy.Field() # the first name of the set / the stock name of the set on the first two cards
    set_name_final = scrapy.Field() # the final name of the set / the unique name of the set on the last card
    set_position = scrapy.Field() # the order by which the cards are in the set
    card_stat_display = scrapy.Field() # the types of stats to display for a card. if 1, it's just base. 2 is base, 2MAX, 2STOCK. 3 is base, 3MAX, 3STOCK, 4MAX, 4STOCK. anything else will be for exceptions.
    set_size = scrapy.Field() # amount of cards in the set
    set_type = scrapy.Field() # type of set (is it normal, mirror, switch, birthday, relationship, memorial, and whatnot)
    set_rarity = scrapy.Field() # highest rarity of the card in the set

    # FOREIGN KEY
    girl_id = scrapy.Field()

    flagged = scrapy.Field()

    # English fields
    set_name_initial_eng = scrapy.Field()
    set_name_final_eng = scrapy.Field()
    name_eng = scrapy.Field()
    skill_name_eng = scrapy.Field()
    description_eng = scrapy.Field()
    set_type = scrapy.Field()

    # extra fields
    translation_status = scrapy.Field() # 0 is not translated, 1 is not verified, 2 is verified, 3 is confirmed
    stat_status = scrapy.Field() # 0 is missing, 1 is auto-generated or crawled from gamy, 2 is not verified, 3 is verified
    information_missing = scrapy.Field() # 0 is not missing, 1 is missing


    # note: to get stats, users should just provide the new BASE and BASEMAX of the card that they're trying to add information for
    # those two stats should be enough to autogenerate everything. The user will be shown what the autogenerated stats are, and they can modify those if there is a slight error (<2%)
    # if the error is larger, the card should be flagged

    # flags:
    #   1: missing girl name in dictionary. is this some sort of hybrid?
    #   2: girl name doesn't match throughout the evolution of the card
    #   3: there are not 3 cards in the set
    #   4: the card is a standalone, or is missing references
    #   5: infinite looping is happening
