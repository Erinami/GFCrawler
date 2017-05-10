# -*- coding: utf8 -*-
# GFKARI CARD CRAWLER
# Version 1.0 - working for all cards that are sets of 3, but does not process stat information aside from BASEMAX. This is enough for now. Ma
# Part of the GFKARIDATABASE project.

# As a fair warning, BE CAREFUL WHEN EDITING CSV FILES USING EXCEL. Various encoding issues may happen.
# Keep backups of files in case encoding goes horribly wrong.
# To convert properly, first open the CSV in sublime text and save with encoding UTF-8 BOM
# Next, open the file in Excel and then save as an xlsx to preserve changes.
# Close the file and open the xlsx to make sure kanji is still displayed properly.
# For whenever you need to generate a csv with proper encoding again, upload the xlsx to Google Sheets
# Open the table in google sheets, and then download as csv from there. It will then have proper UTF-8 encoding.


import scrapy
import json
import math
from gfkari.items import GfkariItem

class GfkariSpider(scrapy.Spider):
    name = "gfkari"
    allowed_domains = ["gamy.jp", "ameba.jp"]
    start_urls = []
    girlDictionarybyName = {}
    girlDictionarybyName[u"日野奏恵"] = ["Kanae Hino",1]
    girlDictionarybyName[u"伊勢崎郁歩"] = ["Ikuho Isezaki",2]
    girlDictionarybyName[u"林田たまき"] = ["Tamaki Hayashida",3]
    girlDictionarybyName[u"島田泉"] = ["Izumi Shimada",4]
    girlDictionarybyName[u"鍋島ちより"] = ["Chiyori Nabeshima",5]
    girlDictionarybyName[u"小倉愛"] = ["Megumi Ogura",6]
    girlDictionarybyName[u"岩本樹"] = ["Tatsuru Iwamoto",7]
    girlDictionarybyName[u"前田彩賀"] = ["Saika Maeda",8]
    girlDictionarybyName[u"皆藤蜜子"] = ["Mitsuko Kaito",9]
    girlDictionarybyName[u"遠山未涼"] = ["Misuzu Toyama",10]
    girlDictionarybyName[u"伊勢谷里都"] = ["Rito Iseya",11]
    girlDictionarybyName[u"水野楓夏"] = ["Fuka Mizuno",12]
    girlDictionarybyName[u"岸田稚慧"] = ["Chie Kishida",13]
    girlDictionarybyName[u"小泉由佳"] = ["Yuka Koizumi",14]
    girlDictionarybyName[u"緒川唯"] = ["Yui Ogawa",15]
    girlDictionarybyName[u"江藤くるみ"] = ["Kurumi Eto",16]
    girlDictionarybyName[u"東野梓"] = ["Azusa Higashino",17]
    girlDictionarybyName[u"早見英子"] = ["Eiko Hayami",18]
    girlDictionarybyName[u"桐山優月"] = ["Yuzuki Kiriyama",19]
    girlDictionarybyName[u"柊真琴"] = ["Makoto Hiragi",20]
    girlDictionarybyName[u"神崎ミコト"] = ["Mikoto Kanzaki",21]
    girlDictionarybyName[u"円城寺小菊"] = ["Kogiku Enjoji",22]
    girlDictionarybyName[u"西野彩音"] = ["Ayane Nishino",23]
    girlDictionarybyName[u"長谷川美卯"] = ["Miu Hasegawa",24]
    girlDictionarybyName[u"川上瀬莉"] = ["Seri Kawakami",25]
    girlDictionarybyName[u"成瀬まなみ"] = ["Manami Naruse",26]
    girlDictionarybyName[u"一色愛瑠"] = ["Airu Isshiki",27]
    girlDictionarybyName[u"五代律"] = ["Ritsu Godai",28]
    girlDictionarybyName[u"竜ヶ崎珠里椏"] = ["Juria Ryugasaki",29]
    girlDictionarybyName[u"上条るい"] = ["Rui Kamijo",30]
    girlDictionarybyName[u"南條クミコ"] = ["Kumiko Nanjo",31]
    girlDictionarybyName[u"赤瀬川摩姫"] = ["Maki Akasegawa",32]
    girlDictionarybyName[u"雪風真弥"] = ["Maya Yukikaze",33]
    girlDictionarybyName[u"李春燕"] = ["Lee Chunyan",34]
    girlDictionarybyName[u"羽鳥晶"] = ["Akira Hatori",35]
    girlDictionarybyName[u"林田希羅"] = ["Kira Hayashida",36]
    girlDictionarybyName[u"綾小路美麗"] = ["Mirei Ayanokoji",37]
    girlDictionarybyName[u"皆口英里"] = ["Eri Minaguchi",38]
    girlDictionarybyName[u"山田はな"] = ["Hana Yamada",39]
    girlDictionarybyName[u"高崎瑠依"] = ["Rui Takasaki",40]
    girlDictionarybyName[u"新垣雛菜"] = ["Hina Nigaki",41]
    girlDictionarybyName[u"八束由紀恵"] = ["Yukie Yatsuka",42]
    girlDictionarybyName[u"櫻井明音"] = ["Akane Sakurai",43]
    girlDictionarybyName[u"山野こだま"] = ["Kodama Yamano",44]
    girlDictionarybyName[u"白鳥詩織"] = ["Shiori Shiratori",45]
    girlDictionarybyName[u"ユーリヤ・ヴャルコワ"] = ["Yulia Valkova",46]
    girlDictionarybyName[u"新田萌果"] = ["Moeka Nitta",47]
    girlDictionarybyName[u"南田七星"] = ["Nanase Minamida",48]
    girlDictionarybyName[u"正岡真衣"] = ["Mai Masaoka",49]
    girlDictionarybyName[u"重藤秋穂"] = ["Akiho Shigeto",50]
    girlDictionarybyName[u"見吉奈央"] = ["Nao Miyoshi",51]
    girlDictionarybyName[u"黒川凪子"] = ["Nagiko Kurokawa",52]
    girlDictionarybyName[u"小野寺千鶴"] = ["Chizuru Onodera",53]
    girlDictionarybyName[u"熊田一葉"] = ["Kazuha Kumada",54]
    girlDictionarybyName[u"掛井園美"] = ["Sonomi Kakei",55]
    girlDictionarybyName[u"大山真由里"] = ["Mayuri Oyama",56]
    girlDictionarybyName[u"玉井麗巳"] = ["Remi Tamai",57]
    girlDictionarybyName[u"優木苗"] = ["Nae Yuki",58]
    girlDictionarybyName[u"東雲レイ"] = ["Rei Shinonome",59]
    girlDictionarybyName[u"湯川基世"] = ["Kise Yukawa",60]
    girlDictionarybyName[u"小日向いちご"] = ["Ichigo Kohinata",61]
    girlDictionarybyName[u"ミス・モノクローム"] = ["Miss Monochrome", 62]
    girlDictionarybyName[u"姫島木乃子"] = ["Kinoko Himejima",63]
    girlDictionarybyName[u"クロエ・ルメール"] = ["Chloe Lemaire",64]
    girlDictionarybyName[u"椎名心実"] = ["Kokomi Shina",65]
    girlDictionarybyName[u"月白陽子"] = ["Yoko Tsukishiro",66]
    girlDictionarybyName[u"村上文緒"] = ["Fumio Murakami",67]
    girlDictionarybyName[u"霧生典子"] = ["Noriko Kiryu",68]
    girlDictionarybyName[u"古谷朱里"] = ["Shuri Furuya",69]
    girlDictionarybyName[u"戸村美知留"] = ["Michiru Tomura",70]
    girlDictionarybyName[u"佐伯鞠香"] = ["Marika Saeki",71]
    girlDictionarybyName[u"夢前春瑚"] = ["Haruko Yumesaki",72]
    girlDictionarybyName[u"飛原鋭子"] = ["Eiko Hibara",73]
    girlDictionarybyName[u"不知火五十鈴"] = ["Isuzu Shiranui",74]
    girlDictionarybyName[u"望月エレナ"] = ["Erena Mochizuki",75]
    girlDictionarybyName[u"鈴河凜乃"] = ["Rino Suzukawa",76]
    girlDictionarybyName[u"笹原野々花"] = ["Nonoka Sasahara",77]
    girlDictionarybyName[u"神楽坂砂夜"] = ["Saya Kagurazaka",78]
    girlDictionarybyName[u"春宮つぐみ"] = ["Tsugumi Harumiya",79]
    girlDictionarybyName[u"螺子川来夢"] = ["Raimu Nejikawa",80]
    girlDictionarybyName[u"宮内希"] = ["Nozomi Miyauchi",81]
    girlDictionarybyName[u"久保田友季"] = ["Yuki Kubota",82]
    girlDictionarybyName[u"荒井薫"] = ["Kaoru Arai",83]
    girlDictionarybyName[u"音羽ユリ"] = ["Yuri Otowa",84]
    girlDictionarybyName[u"浅見景"] = ["Kei Asami",85]
    girlDictionarybyName[u"芹那"] = ["Serina", 86]
    girlDictionarybyName[u"吉川繭子"] = ["Mayuko Yoshikawa",87]
    girlDictionarybyName[u"三科果歩"] = ["Kaho Mishina",88]
    girlDictionarybyName[u"橘響子"] = ["Kyoko Tachibana",92]
    girlDictionarybyName[u"弓削楓"] = ["Kaede Yuge",93]
    girlDictionarybyName[u"鴫野睦"] = ["Mutsumi Shigino",97]
    girlDictionarybyName[u"森園芽以"] = ["Mei Morizono",98]
    girlDictionarybyName[u"葉月柚子"] = ["Yuzuko Hazuki",99]
    girlDictionarybyName[u"九重忍"] = ["Shinobu Kokonoe",100]
    girlDictionarybyName[u"朝比奈桃子"] = ["Momoko Asahina",101]
    girlDictionarybyName[u"畑山政子"] = ["Masako Hatayama",102]
    girlDictionarybyName[u"加賀美茉莉"] = ["Matsuri Kagami",103]
    girlDictionarybyName[u"甘利燈"] = ["Akari Amari",104]
    girlDictionarybyName[u"石田いすき"] = ["Isuki Ishida",109]
    girlDictionarybyName[u"夏目真尋"] = ["Mahiro Natsume",110]
    girlDictionarybyName[u"天都かなた"] = ["Kanata Amatsu",111]
    girlDictionarybyName[u"有栖川小枝子"] = ["Saeko Arisugawa",112]
    girlDictionarybyName[u"君嶋里琉"] = ["Satoru Kimijima",113]
    girlDictionarybyName[u"時谷小瑠璃"] = ["Koruri Tokitani",115]
    girlDictionarybyName[u"三嶋ゆらら"] = ["Yurara Mishima",116]
    girlDictionarybyName[u"押井知"] = ["Tomo Oshi",117]
    girlDictionarybyName[u"白瀬つづり"] = ["Tsuzuri Shirase",119]
    girlDictionarybyName[u"風町陽歌"] = ["Haruka Kazemachi",120]
    girlDictionarybyName[u"相楽エミ"] = ["Emi Sagara",121]
    girlDictionarybyName[u"千代浦あやめ"] = ["Ayame Chiyoura",122]
    girlDictionarybyName[u"栢嶋乙女"] = ["Otome Kayashima",123]
    girlDictionarybyName[u"川淵一美"] = ["Kazumi Kawabuchi",124]
    girlDictionarybyName[u"芙来田伊吹"] = ["Ibuki Fukita",125]
    girlDictionarybyName[u"橋本環奈"] = ["Kanna Hashimoto", 137]
    girlDictionarybyName[u"武内未美"] = ["Mimi Takeuchi",138]
    girlDictionarybyName[u"蓬田菫"] = ["Sumire Yomogida",148]
    girlDictionarybyName[u"篠宮りさ"] = ["Risa Shinomiya",156]
    girlDictionarybyName[u"七海四季"] = ["Shiki Nanami",164]
    girlDictionarybyName[u"織部千華"] = ["Chika Oribe",166]
    girlDictionarybyName[u"吉永和花那"] = ["Wakana Yoshinaga",168]
    girlDictionarybyName[u"祐天寺弥生"] = ["Yayoi Yutenji",172]
    girlDictionarybyName[u"深見絵真"] = ["Ema Fukami",176]
    girlDictionarybyName[u"花房優輝"] = ["Yuki Hanafusa",179]
    girlDictionarybyName[u"鳴海調"] = ["Shirabe Narumi",180]
    girlDictionarybyName[u"反町牡丹"] = ["Botan Sorimachi",183]
    girlDictionarybyName[u"浮橋明日香"] = ["Asuka Ukihashi",184]
    girlDictionarybyName[u"直江悠"] = ["Yu Naoe",185]
    girlDictionarybyName[u"朝門春日"] = ["Kasuga Asato",194]
    girlDictionarybyName[u"牧瀬昴"] = ["Subaru Makise",195]
    girlDictionarybyName[u"久仁城雅"] = ["Miyabi Kunishiro",196]
    girlDictionarybyName[u"藤堂静子"] = ["Shizuko Todo",199]
    girlDictionarybyName[u"真白透子"] = ["Toko Mashiro",200]
    girlDictionarybyName[u"豊永日々喜"] = ["Hibiki Toyonaga",202]
    girlDictionarybyName[u"アネット・オルガ・唐澤"] = ["Anette Olga Karasawa",203]
    girlDictionarybyName[u"三条八重"] = ["Yae Sanjo",204]
    girlDictionarybyName[u"高良美空"] = ["Sora Takara",208]
    girlDictionarybyName[u"高良美海"] = ["Umi Takara",209]
    girlDictionarybyName[u"鹿目まどか"] = ["Madoka Kaname", 212]
    girlDictionarybyName[u"暁美ほむら"] = ["Homura Akemi", 213]
    girlDictionarybyName[u"巴マミ"] = ["Mami Tomoe", 214]
    girlDictionarybyName[u"美樹さやか"] = ["Sayaka Miki", 215]
    girlDictionarybyName[u"佐倉杏子"] = ["Kyouko Sakura", 216]
    girlDictionarybyName[u"志筑仁美"] = ["Hitomi Shizuki", 217]
    girlDictionarybyName[u"ココア"] = ["Cocoa", 219]
    girlDictionarybyName[u"チノ"] = ["Chino", 220]
    girlDictionarybyName[u"リゼ"] = ["Rize", 221]
    girlDictionarybyName[u"千夜"] = ["Chiya", 222]
    girlDictionarybyName[u"シャロ"] = ["Sharo", 223]


    def __init__(self):
        for i in range(1100):
            self.start_urls.append("https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(7526 + i))

    def parse(self, response):
        item = GfkariItem()

        # get the data array, and process it as a json
        locations = response.xpath('//script[contains(., "var GAMY_DICTIONARY_ITEM_DATA")]/text()').extract()
        start = locations[0].find("{")
        end = locations[0].find("};") + 1
        variable = locations[0][start:end]
        variable = json.loads(variable)
        url = response.url
        start = url.find("girls/") + 6
        item["card_id"] = url[start:len(url)]

        # normalization of unicode characters
        variable["name"] = variable["name"].replace(u"＋", "+")
        variable["name"] = variable["name"].replace(u"］", "]")
        variable["name"] = variable["name"].replace(u"［", "[")

        # read values from the json and set them accordingly. the if statements are below are to resolve naming differences
        for title, data in variable.iteritems():
            if (title == "strongest_attack"):
                item["strongest_attack_base"] = data
            elif (title == "strongest_defense"):
                item["strongest_defense_base"] = data
            elif (title == "max_attack"):
                item["max_attack_base"] = data
            elif (title == "max_defense"):
                item["max_defense_base"] = data
            elif (title == "initial_defense"):
                item["initial_defense_base"] = data
            elif (title == "initial_attack"):
                item["initial_attack_base"] = data
            elif (title == "image"):
                item["image_url"] = data;
            else:
                item[title] = data

        # currently, there should be no problems with the card, so let's NOT flag the card for review. We'll flag it if we find anything weird.
        # also, set the type to normal, since that's our initial assumption for all cards. if only they were actually just normal...
        item["flagged"] = 0
        item["set_type"] = "normal"

        # normalization replacement of various unicode characters
        item["name"] = item["name"].replace(u"＋", "+")
        item["name"] = item["name"].replace(u"］", "]")
        item["name"] = item["name"].replace(u"［", "[")

        # let's find the girl associated with this card by reading the card name. The girl's name will always come after the [xxx].
        girlName = item["name"]
        start = girlName.find("]") + 1
        if (u"］" in girlName):
            start = girlName.find(u"］") + 1

        # check if there's a plus in the card, if so, we the last character of the card (which should be the plus)
        girlName = girlName.strip()
        lastChar = girlName[-1:]
        if ("+" in lastChar) or (u"＋" in lastChar):
            girlName = girlName[start:(len(girlName) - 1)]
        else:
            girlName = girlName[start:(len(girlName))] # else, just read everything from after the brackets to the end

        print girlName
        if u"＋" in lastChar:
            item["name"] = item["name"][:-1] + "+"
        # make sure the girl name deciphered is part of the dictionary. if not, we FLAG the card for further manual review, because we have no clue what's going on
        if girlName in self.girlDictionarybyName:
            item["girl_id"] = self.girlDictionarybyName[girlName][1]
        else:
            item["flagged"] = 1
        # now, we need to find some set information and stat information by doing some recursion.
        # NOTE: Mathematical calculations will ASSUME that the card set consists of three cards! Otherwise, the math will be INCORRECT and must be handled manually.
        # if the card appears to be a standalone
        if item["before_evolution_uid"] is None and item["evolution_uid"] is None:
            # flag it, then set everything as you would it the first card in a set (without the forwards recursion)
            item["flagged"] = 4
            item["set_size"] = 1
            item["set_position"] = 1
            item["card_stat_display"] = 1
            item["set_id"] = item["card_id"]
            start = item["name"].find("[") + 1
            end = item["name"].find("]")
            item["set_rarity"] = variable["rarity"]
            if '[' not in item["name"]:
                item["set_name_initial"] = u"ストック"
                item["set_name_initial_eng"] = "Stock"
            else:
                item["set_name_initial"] = item["name"][start:end]
            yield item
        # if the card we're looking at has no previous links:
        elif item["before_evolution_uid"] is None:
            # the card has only a BASEMAX stat, so there's no need to do any more mathematical calculations either
            item["set_position"] = 1
            item["card_stat_display"] = 1
            item["set_id"] = item["card_id"]
            start = item["name"].find("[") + 1
            end = item["name"].find("]")
            if '[' not in item["name"]:
                item["set_name_initial"] = u"ストック"
                item["set_name_initial_eng"] = "Stock"
            else:
                item["set_name_initial"] = item["name"][start:end]
            # now, we're missing the set_name_final field of the card. we have to get this by recursively going to the card's next links.
            url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(item["evolution_uid"])
            request = scrapy.Request(url=url, callback=self.parse_forward_recursion, dont_filter=True)
            request.meta['item'] = item
            request.meta['traversed'] = 0
            yield request
        # if the card has no forward links
        elif item["evolution_uid"] is None:
            # we know the set's final name (since this is the last card), so let's set that
            item["set_rarity"] = variable["rarity"]
            start = variable["name"].find("[") + 1
            end = variable["name"].find("]")
            item["set_name_final"] = variable["name"][start:end]

            # we need to find the card's position relative to the starting card. we'll need to do backwards recursion all the way to the first card of the set
            url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(item["before_evolution_uid"])
            request = scrapy.Request(url=url, callback=self.parse_backwards_recursion, dont_filter=True)
            request.meta['item'] = item
            request.meta['traversed'] = 0
            basestats = {}
            basestats[0] = [item["initial_attack_base"], item["initial_defense_base"], item["max_attack_base"], item["max_defense_base"]]
            request.meta['basestats'] = basestats
            # checking for special cases
            if u"ミラーガール" in variable["name"]:
                item["set_type"] = "mirror"
                request.meta['special'] = 'mirror'
                item["flagged"] = 0
                item["set_name_final"] = u"ミラーガール"
                item["set_name_final_eng"] = "Mirror Girl"
            elif u"スイッチガール" in variable["name"]:
                item["set_type"] = "switch"
                item["flagged"] = 0
                item["set_name_final"] = u"スイッチガール"
                item["set_name_final_eng"] = "Switch Girl"
            elif u"プリズムガール" in variable["name"]:
                item["set_type"] = "prism"
                item["flagged"] = 0
                item["set_name_final"] = u"プリズムガール"
                item["set_name_final_eng"] = "Prism Girl"
            yield request
        else:
            # if we're smack in the middle, we're gonna do forward recursion first and then do backwards recursion
            url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(item["evolution_uid"])
            request = scrapy.Request(url=url, callback=self.parse_forward_recursion, dont_filter=True)
            request.meta['item'] = item
            request.meta['traversed'] = 0
            yield request

    # oh baby here's where the real chunky mess of mathematical calculations are
    def parse_backwards_recursion(self, response):
        # get the data array, and process it as a json
        traversed = response.meta["traversed"] + 1
        item = response.meta["item"]
        if traversed > 25:
            item["flagged"] = 5
            yield item
            return
        basestats = response.meta["basestats"]
        locations = response.xpath('//script[contains(., "var GAMY_DICTIONARY_ITEM_DATA")]/text()').extract()
        start = locations[0].find("{")
        end = locations[0].find("};") + 1
        variable = locations[0][start:end]
        variable = json.loads(variable)
        prevLink = variable["before_evolution_uid"]

        variable["name"] = variable["name"].replace(u"＋", "+")
        variable["name"] = variable["name"].replace(u"］", "]")
        variable["name"] = variable["name"].replace(u"［", "[")

        # do a check on this card to make sure that the name of the girl on this card is the same as the card we came from. otherwise, flag it.
        if item["flagged"] == 0:
            girlName = variable["name"]
            start = girlName.find("]") + 1
            # check if there's a plus in the card, if so, we the last character of the card (which should be the plus)
            if (u"］" in girlName):
                start = girlName.find(u"］") + 1
            girlName = girlName.strip()
            lastChar = girlName[-1:]
            if ("+" in lastChar) or (u"＋" in lastChar):
                girlName = girlName[start:(len(girlName) - 1)]
            else:
                girlName = girlName[start:(len(girlName))] # else, just read everything from after the brackets to the end
            # make sure the girl name deciphered is part of the dictionary. if not, we FLAG the card for further manual review, because we have no clue what's going on
            if girlName in self.girlDictionarybyName:
                finalGirlID = self.girlDictionarybyName[girlName][1]
                if item["girl_id"] != finalGirlID:
                    item["flagged"] = 2
            else:
                item["flagged"] = 1

        # if there's no previous link, we're gonna do our job here
        if prevLink is None:
            # check if the card we're coming from had a next link, as if it didn't we only have one traversed variable we're dealing with
            # thus, the amount of cards in the set is just that one traversed variable, not the sum of prevTraversed and forwardsTraversed.
            if item["evolution_uid"] is None:
                item["set_size"] = traversed + 1
            else:
                item["set_size"] = traversed + response.meta["forwardsTraversed"] + 1
            if item["set_size"] != 3:
                if item["flagged"] == 0:
                    item["flagged"] = 3
            item["set_position"] = traversed + 1
            item["card_stat_display"] = traversed + 1
            if item["card_stat_display"] > 3:
                item["card_stat_display"] = 3
            url = response.url
            start = url.find("girls/") + 6
            firstCardID = url[start:len(url)]
            item["set_id"] = firstCardID
            start = variable["name"].find("[") + 1
            end = variable["name"].find("]")
            if '[' not in variable["name"]:
                item["set_name_initial"] = u"ストック"
                item["set_name_initial_eng"] = "Stock"
            else:
                item["set_name_initial"] = variable["name"][start:end]

            # card stat display changes for the special types that can be accounted for (mirror/switch/prism)
            # all of the below values are SPECULATION ONLY. they are GUARANTEED to be INCORRECT.
            # i don't have any idea how these values are calculated for mirror/switch/prism/gift/date/ribbon girls, so i'm just doing whatever i feel is close to being legit
            if item["set_position"] == 3:
                print "THIS IS FOR THE 3RD CARD"
                print basestats
            cardType = item["set_type"];
            if "mirror" in cardType: # i'm assuming mirror cards get atk+def switched.
                item["flagged"] = 0
                if item["set_position"] == 4:
                    item["card_stat_display"] = 3
                    basestats[1] = basestats[2]
                    temp = basestats[1][0]
                    basestats[1][0] = basestats[1][1]
                    basestats[1][1] = temp
                    temp = basestats[1][2]
                    basestats[1][2] = basestats[1][3]
                    basestats[1][3] = temp
                    temp = variable["max_defense"]
                    variable["max_defense"] = variable["max_attack"]
                    variable["max_attack"] = temp
                    temp = variable["initial_defense"]
                    variable["initial_defense"] = variable["initial_attack"]
                    variable["initial_attack"] = temp
            elif "switch" in cardType: # seems like their stats remain the same whether ON or OFF.
                item["flagged"] = 0
                if item["set_position"] == 4:
                    item["card_stat_display"] = 3
                    basestats[1] = basestats[2]
                    print basestats
            elif "prism" in cardType: # i have no clue what's going on, gonna assume that it uses the first two cards in the set like normal.
                item["flagged"] = 0
                if item["set_position"] == 4:
                    item["card_stat_display"] = 3
                    basestats[1] = basestats[2]
                elif item["set_position"] == 5:
                    item["card_stat_display"] = 3
                    basestats[1] = basestats[3]

            # do mathematical stat calculations here
            # this is where everythings gets completely ugly and disgusting
            # NOTE: in order to successfully calculate all stats, the BASE (initial value) and BASEMAX (card at max level with no cheer force transferred over)
            # must be avaliable for use. Unfortunately, Gamy's BASEMAX values are approximated, and are generally wrong. The error is minimal for cards with a higher
            # cost of =>13 (usually less than 5%), but are pretty high for lower cost value cards (up to 25%).
            #
            # For the sake of the crawler, we are assuming that Gamy's values are fully correct. However, in the actual web application, a verification and easy
            # modification system that allows users to input a BASE and BASEMAX value for each card will be necessary to accurately generate stats.
            #
            # This also means that all cards are going to need additional verification values in the database. Oh boy. This is a TODO, and a big one at that.
            #
            # if this is the 2nd card (2MAX and 2STOCK)
            if item["card_stat_display"] == 2:
                initial_attack_2MAX = math.ceil(float(variable["max_attack"]) * .1 + float(variable["max_attack"]) * .1 + float(basestats[0][0]))
                max_attack_2MAX = math.ceil(float(variable["max_attack"]) * .1 + float(variable["max_attack"]) * .1 + float(basestats[0][2]))
                strongest_attack_2MAX = math.ceil(max_attack_2MAX * 1.20)
                initial_defense_2MAX = math.ceil(float(variable["max_defense"]) * .1 + float(variable["max_defense"]) * .1 + float(basestats[0][1]))
                max_defense_2MAX = math.ceil(float(variable["max_defense"]) * .1 + float(variable["max_defense"]) * .1 + float(basestats[0][3]))
                strongest_defense_2MAX = math.ceil(max_defense_2MAX * 1.20)

                initial_attack_2STOCK = math.ceil(float(variable["initial_attack"]) * .1 + float(variable["initial_attack"]) * .1 + float(basestats[0][0]))
                max_attack_2STOCK = math.ceil(float(variable["initial_attack"]) * .1 + float(variable["initial_attack"]) * .1 + float(basestats[0][2]))
                strongest_attack_2STOCK = math.ceil(max_attack_2STOCK * 1.20)
                initial_defense_2STOCK = math.ceil(float(variable["initial_defense"]) * .1 + float(variable["initial_defense"]) * .1 + float(basestats[0][1]))
                max_defense_2STOCK = math.ceil(float(variable["initial_defense"]) * .1 + float(variable["initial_defense"]) * .1 + float(basestats[0][3]))
                strongest_defense_2STOCK = math.ceil(max_defense_2STOCK * 1.20)

                item["initial_attack_2MAX"] = initial_attack_2MAX
                item["max_attack_2MAX"] = max_attack_2MAX
                item["strongest_attack_2MAX"] = strongest_attack_2MAX
                item["initial_defense_2MAX"] = initial_defense_2MAX
                item["max_defense_2MAX"] = max_defense_2MAX
                item["strongest_defense_2MAX"] = strongest_defense_2MAX
                item["initial_attack_2STOCK"] = initial_attack_2STOCK
                item["max_attack_2STOCK"] = max_attack_2STOCK
                item["strongest_attack_2STOCK"] = strongest_attack_2STOCK
                item["initial_defense_2STOCK"] = initial_defense_2STOCK
                item["max_defense_2STOCK"] = max_defense_2STOCK
                item["strongest_defense_2STOCK"] = strongest_defense_2STOCK

            # if this is the 3rd card (4MAX 3STOCK 4MAX 4STOCK)
            elif item["card_stat_display"] == 3:
                print basestats[1]
                print basestats[0]
                initial_attack_2MAX = math.ceil(float(variable["max_attack"]) * .1 + float(variable["max_attack"]) * .1 + float(basestats[1][0]))
                max_attack_2MAX = math.ceil(float(variable["max_attack"]) * .1 + float(variable["max_attack"]) * .1 + float(basestats[1][2]))
                strongest_attack_2MAX = math.ceil(max_attack_2MAX * 1.20)
                initial_defense_2MAX = math.ceil(float(variable["max_defense"]) * .1 + float(variable["max_defense"]) * .1 + float(basestats[1][1]))
                max_defense_2MAX = math.ceil(float(variable["max_defense"]) * .1 + float(variable["max_defense"]) * .1 + float(basestats[1][3]))
                strongest_defense_2MAX = math.ceil(max_defense_2MAX * 1.20)

                initial_attack_2STOCK = math.ceil(float(variable["initial_attack"]) * .05 + float(variable["initial_attack"]) * .05 + float(basestats[1][0]))
                max_attack_2STOCK = math.ceil(float(variable["initial_attack"]) * .05 + float(variable["initial_attack"]) * .05 + float(basestats[1][2]))
                strongest_attack_2STOCK = math.ceil(max_attack_2STOCK * 1.20)
                initial_defense_2STOCK = math.ceil(float(variable["initial_defense"]) * .05 + float(variable["initial_defense"]) * .05 + float(basestats[1][1]))
                max_defense_2STOCK = math.ceil(float(variable["initial_defense"]) * .05 + float(variable["initial_defense"]) * .05 + float(basestats[1][3]))
                strongest_defense_2STOCK = math.ceil(max_defense_2STOCK * 1.20)

                print strongest_defense_2MAX
                print strongest_attack_2MAX
                initial_attack_4MAX = math.ceil(max_attack_2MAX * .1 + max_attack_2MAX * .1 + float(basestats[0][0]))
                max_attack_4MAX = math.ceil(max_attack_2MAX * .1 + max_attack_2MAX * .1 + float(basestats[0][2]))
                strongest_attack_4MAX = math.ceil(max_attack_4MAX * 1.20)
                initial_defense_4MAX = math.ceil(max_defense_2MAX * .1 + max_defense_2MAX * .1 + float(basestats[0][1]))
                max_defense_4MAX = math.ceil(max_defense_2MAX * .1 + max_defense_2MAX * .1 + float(basestats[0][3]))
                strongest_defense_4MAX = math.ceil(max_defense_4MAX * 1.20)

                initial_attack_4STOCK = math.ceil(max_attack_2STOCK * .1 + max_attack_2STOCK * .1 + float(basestats[0][0]))
                max_attack_4STOCK = math.ceil(max_attack_2STOCK * .1 + max_attack_2STOCK * .1 + float(basestats[0][2]))
                strongest_attack_4STOCK = math.ceil(max_attack_4STOCK * 1.20)
                initial_defense_4STOCK = math.ceil(max_defense_2STOCK * .1 + max_defense_2STOCK * .1 + float(basestats[0][1]))
                max_defense_4STOCK = math.ceil(max_defense_2STOCK * .1 + max_defense_2STOCK * .1 + float(basestats[0][3]))
                strongest_defense_4STOCK = math.ceil(max_defense_4STOCK * 1.20)

                initial_attack_3MAX = math.ceil(max_attack_2MAX * .1 + float(variable["max_attack"]) * .1 + float(basestats[0][0]))
                max_attack_3MAX = math.ceil(max_attack_2MAX * .1 + float(variable["max_attack"]) * .1 + float(basestats[0][2]))
                strongest_attack_3MAX = math.ceil(max_attack_3MAX * 1.20)
                initial_defense_3MAX = math.ceil(max_defense_2MAX * .1 + float(variable["max_defense"]) * .1 + float(basestats[0][1]))
                max_defense_3MAX = math.ceil(max_defense_2MAX * .1 + float(variable["max_defense"]) * .1 + float(basestats[0][3]))
                strongest_defense_3MAX = math.ceil(max_defense_3MAX * 1.20)

                initial_attack_3STOCK = math.ceil(max_attack_2STOCK * .1 + float(variable["initial_attack"]) * .1 + float(basestats[0][0]))
                max_attack_3STOCK = math.ceil(max_attack_2STOCK * .1 + float(variable["initial_attack"]) * .1 + float(basestats[0][2]))
                strongest_attack_3STOCK = math.ceil(max_attack_3STOCK * 1.20)
                initial_defense_3STOCK = math.ceil(max_defense_2STOCK * .1 + float(variable["initial_defense"]) * .1 + float(basestats[0][1]))
                max_defense_3STOCK = math.ceil(max_defense_2STOCK * .1 + float(variable["initial_defense"]) * .1 + float(basestats[0][3]))
                strongest_defense_3STOCK = math.ceil(max_defense_3STOCK * 1.20)

                item["initial_attack_4MAX"] = initial_attack_4MAX
                item["max_attack_4MAX"] = max_attack_4MAX
                item["strongest_attack_4MAX"] = strongest_attack_4MAX
                item["initial_defense_4MAX"] = initial_defense_4MAX
                item["max_defense_4MAX"] = max_defense_4MAX
                item["strongest_defense_4MAX"] = strongest_defense_4MAX

                item["initial_attack_4STOCK"] = initial_attack_4STOCK
                item["max_attack_4STOCK"] = max_attack_4STOCK
                item["strongest_attack_4STOCK"] = strongest_attack_4STOCK
                item["initial_defense_4STOCK"] = initial_defense_4STOCK
                item["max_defense_4STOCK"] = max_defense_4STOCK
                item["strongest_defense_4STOCK"] = strongest_defense_4STOCK

                item["initial_attack_3MAX"] = initial_attack_3MAX
                item["max_attack_3MAX"] = max_attack_3MAX
                item["strongest_attack_3MAX"] = strongest_attack_3MAX
                item["initial_defense_3MAX"] = initial_defense_3MAX
                item["max_defense_3MAX"] = max_defense_3MAX
                item["strongest_defense_3MAX"] = strongest_defense_3MAX

                item["initial_attack_3STOCK"] = initial_attack_3STOCK
                item["max_attack_3STOCK"] = max_attack_3STOCK
                item["strongest_attack_3STOCK"] = strongest_attack_3STOCK
                item["initial_defense_3STOCK"] = initial_defense_3STOCK
                item["max_defense_3STOCK"] = max_defense_3STOCK
                item["strongest_defense_3STOCK"] = strongest_defense_3STOCK
            else:
                # by error handling above, we should have already flagged this card, but it doesn't hurt to do it again
                item["flagged"] = 3

            # WE'RE DONE BOYS
            yield item
        else: # otherwise, let's keep this recursion going
            url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(variable["before_evolution_uid"])
            request = scrapy.Request(url=url, callback=self.parse_backwards_recursion, dont_filter=True)
            request.meta['item'] = item
            request.meta['traversed'] = traversed
            if 'forwardsTraversed' in response.meta:
                request.meta['forwardsTraversed'] = response.meta['forwardsTraversed']
            if 'special' in response.meta:
                request.meta['special'] = response.meta['special']
            # adds this card's basestats to the array as well, since it will also have to be used for calculations
            basestatCount = len(basestats)
            basestats[basestatCount] = [variable["initial_attack"], variable["initial_defense"], variable["max_attack"], variable["max_defense"]]
            request.meta['basestats'] = basestats
            yield request

    # Forward recursion is simpler than backwards recursion, since we don't need to keep track of base stats (since calculations are only done once we've hit the first card in the set)
    # All we need to do is keep going forward until we can't go forward any more
    # Then, do some quick checking to see how many cards we've gone through to hit that point, and then set set_name_final accordingly (or flag the card for further review)
    def parse_forward_recursion(self, response):

        # get the data array, and process it as a json
        traversed = response.meta["traversed"] + 1
        item = response.meta["item"]
        if traversed > 25:
            item["flagged"] = 5
            yield item
            return
        locations = response.xpath('//script[contains(., "var GAMY_DICTIONARY_ITEM_DATA")]/text()').extract()
        start = locations[0].find("{")
        end = locations[0].find("};") + 1
        variable = locations[0][start:end]
        variable = json.loads(variable)
        nextLink = variable["evolution_uid"]

        # normalization of unicode characters
        variable["name"] = variable["name"].replace(u"＋", "+")
        variable["name"] = variable["name"].replace(u"］", "]")
        variable["name"] = variable["name"].replace(u"［", "[")

        # do a check on this card to make sure that the name of the girl on this card is the same as the card we came from. otherwise, flag it.
        if item["flagged"] == 0:
            girlName = variable["name"]
            start = girlName.find("]") + 1
            if (u"］" in girlName):
                start = girlName.find(u"］") + 1
            # check if there's a plus in the card, if so, we the last character of the card (which should be the plus)
            girlName = girlName.strip()
            lastChar = girlName[-1:]
            if ("+" in lastChar) or (u"＋" in lastChar):
                girlName = girlName[start:(len(girlName) - 1)]
            else:
                girlName = girlName[start:(len(girlName))] # else, just read everything from after the brackets to the end
            # make sure the girl name deciphered is part of the dictionary. if not, we FLAG the card for further manual review, because we have no clue what's going on
            if girlName in self.girlDictionarybyName:
                finalGirlID = self.girlDictionarybyName[girlName][1]
                if item["girl_id"] != finalGirlID:
                    item["flagged"] = 2
            else:
                item["flagged"] = 1

        # if there's no next link, we're gonna do our job here
        if nextLink is None:
            # check if the card we're coming from had a previous link
            # if it didn't, it's definitely the first card in the set so we don't need ot call parse_backwards_recursion from here
            # we also do error flagging here based on set size since we know how many cards are in the set already
            item["set_rarity"] = variable["rarity"]
            if item["before_evolution_uid"] is None:
                # flag the card if there are not 3 cards in the set
                if item["flagged"] == 0:
                    if traversed + item["set_position"] != 3:
                        item["flagged"] = 3
                # let's set the last variables that we need
                start = variable["name"].find("[") + 1
                end = variable["name"].find("]")
                item["set_name_final"] = variable["name"][start:end]
                item["set_size"] = traversed + 1

                # checking for special cases
                if u"ミラーガール" in variable["name"]:
                    item["set_type"] = "mirror"
                    item["flagged"] = 0
                    item["set_name_final"] = u"ミラーガール"
                    item["set_name_final_eng"] = "Mirror Girl"
                elif u"スイッチガール" in variable["name"]:
                    item["set_type"] = "switch"
                    item["flagged"] = 0
                    item["set_name_final"] = u"スイッチガール"
                    item["set_name_final_eng"] = "Switch Girl"
                elif u"プリズムガール" in variable["name"]:
                    item["set_type"] = "prism"
                    item["flagged"] = 0
                    item["set_name_final"] = u"プリズムガール"
                    item["set_name_final_eng"] = "Prism Girl"

                yield item  # yield the item because we're done with it now
            # otherwise, that means that there were cards previous to the one we started working with
            # that means now we have to call backwards recursion on the card we started with to fill in the rest of the information after we set the info we needed from here
            else:
                # since we're at the final card, we know what set_name_final should be, but nothing else can be set here
                start = variable["name"].find("[") + 1
                end = variable["name"].find("]")
                item["set_name_final"] = variable["name"][start:end]
                # now, let's recurse from the original card all the way to its first card (opposite direction recursion)
                url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(item["before_evolution_uid"])
                request = scrapy.Request(url=url, callback=self.parse_backwards_recursion, dont_filter=True)
                request.meta['item'] = item
                request.meta['traversed'] = 0
                request.meta['forwardsTraversed'] = traversed # we need to store the amount of recursions we did forward so we know the size of the set in general
                # also need to pass basestats over from the original starting card
                basestats = {}
                basestats[0] = [item["initial_attack_base"], item["initial_defense_base"], item["max_attack_base"], item["max_defense_base"]]
                request.meta['basestats'] = basestats

                # checking for special cases
                if u"ミラーガール" in variable["name"]:
                    item["set_type"] = "mirror"
                    request.meta['special'] = 'mirror'
                    item["flagged"] = 0
                    item["set_name_final"] = u"ミラーガール"
                    item["set_name_final_eng"] = "Mirror Girl"
                elif u"スイッチガール" in variable["name"]:
                    item["set_type"] = "switch"
                    item["flagged"] = 0
                    item["set_name_final"] = u"スイッチガール"
                    item["set_name_final_eng"] = "Switch Girl"
                elif u"プリズムガール" in variable["name"]:
                    item["set_type"] = "prism"
                    item["flagged"] = 0
                    item["set_name_final"] = u"プリズムガール"
                    item["set_name_final_eng"] = "Prism Girl"
                yield request
        else: # otherwise, let's keep this recursion going
            url = "https://gamy.jp/girlfriend-kari/dictionaries/girls/" + str(variable["evolution_uid"])
            request = scrapy.Request(url=url, callback=self.parse_forward_recursion, dont_filter=True)
            request.meta['item'] = item
            request.meta['traversed'] = traversed
            yield request

# alright, so you've finished running it. now what?
# A LOT OF MANUAL WORK.

# FIRST OFF: Separate the card images from the gamy thumbnails, and then use a photoshop macro to generate thumbnails for the card images.
# we'll need thumbnails of all increments of 10% from 10% to 90%. Yes, that's a lot - but photoshop's batch macro will work just perfectly for this.
# Scrapy was supposed to support this out of box, but it's not working. Contact me if you know why.

# SECOND OFF: Take the generated CSV and add a BOM to it, so that it can be opened in Excel. Once in Excel, go through ALL cards that have been flagged and fix them manually. This will probably take hours.
# Make sure to list girl ids as commas for cards with multiple girls (for the time being until the many-to-many table is created)
# Afterwards, run a check to make sure that all card ids are present.

# THIRD OFF: Separate the set information from the card information, and create the set table. Remember, a set is one to many. (future: create category which consists of sets, one to many again)

# FOURTH OFF: Create the many-to-many table for the card-girls relationship.

# FINALLY: Put it into the database and watch as it all goes up in flames - er - works perfectly!

# Running this code is literally just the beginning of the battle. There's still all this translation work that still needs to be done...

# FUTURE: Need to implement a flagging system (many to many with cards) to mark and keep track of issues. Also, we may need a voice table that stores locations of voice clips and link them with cards (one to many)
