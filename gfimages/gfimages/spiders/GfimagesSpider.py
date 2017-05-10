# -*- coding: utf8 -*-
# GFKARI CARD CRAWLER
# Version 1.0 - crawls images from gfkari.gamedbs.jp
# Part of the GFKARIDATABASE project.

import scrapy
import json
import math
import hashlib
import datetime
from gfimages.items import GfimagesItem

class GfimagesSpider(scrapy.Spider):
    name = 'gfimages'
    start_urls = []
    allowed_domains = ["ameba.jp", "gamedbs.jp"]
    girlDictionarybyNumber = {}
    girlDictionarybyNumber[1] = ["Kanae Hino",u"日野奏恵"]
    girlDictionarybyNumber[2] = ["Ikuho Isezaki",u"伊勢崎郁歩"]
    girlDictionarybyNumber[3] = ["Tamaki Hayashida",u"林田たまき"]
    girlDictionarybyNumber[4] = ["Izumi Shimada",u"島田泉"]
    girlDictionarybyNumber[5] = ["Chiyori Nabeshima",u"鍋島ちより"]
    girlDictionarybyNumber[6] = ["Megumi Ogura",u"小倉愛"]
    girlDictionarybyNumber[7] = ["Tatsuru Iwamoto",u"岩本樹"]
    girlDictionarybyNumber[8] = ["Saika Maeda",u"前田彩賀"]
    girlDictionarybyNumber[9] = ["Mitsuko Kaito",u"皆藤蜜子"]
    girlDictionarybyNumber[10] = ["Misuzu Toyama",u"遠山未涼"]
    girlDictionarybyNumber[11] = ["Rito Iseya",u"伊勢谷里都"]
    girlDictionarybyNumber[12] = ["Fuka Mizuno",u"水野楓夏"]
    girlDictionarybyNumber[13] = ["Chie Kishida",u"岸田稚慧"]
    girlDictionarybyNumber[14] = ["Yuka Koizumi",u"小泉由佳"]
    girlDictionarybyNumber[15] = ["Yui Ogawa",u"緒川唯"]
    girlDictionarybyNumber[16] = ["Kurumi Eto",u"江藤くるみ"]
    girlDictionarybyNumber[17] = ["Azusa Higashino",u"東野梓"]
    girlDictionarybyNumber[18] = ["Eiko Hayami",u"早見英子"]
    girlDictionarybyNumber[19] = ["Yuzuki Kiriyama",u"桐山優月"]
    girlDictionarybyNumber[20] = ["Makoto Hiragi",u"柊真琴"]
    girlDictionarybyNumber[21] = ["Mikoto Kanzaki",u"神崎ミコト"]
    girlDictionarybyNumber[22] = ["Kogiku Enjoji",u"円城寺小菊"]
    girlDictionarybyNumber[23] = ["Ayane Nishino",u"西野彩音"]
    girlDictionarybyNumber[24] = ["Miu Hasegawa",u"長谷川美卯"]
    girlDictionarybyNumber[25] = ["Seri Kawakami",u"川上瀬莉"]
    girlDictionarybyNumber[26] = ["Manami Naruse",u"成瀬まなみ"]
    girlDictionarybyNumber[27] = ["Airu Isshiki",u"一色愛瑠"]
    girlDictionarybyNumber[28] = ["Ritsu Godai",u"五代律"]
    girlDictionarybyNumber[29] = ["Juria Ryugasaki",u"竜ヶ崎珠里椏"]
    girlDictionarybyNumber[30] = ["Rui Kamijo",u"上条るい"]
    girlDictionarybyNumber[31] = ["Kumiko Nanjo",u"南條クミコ"]
    girlDictionarybyNumber[32] = ["Maki Akasegawa",u"赤瀬川摩姫"]
    girlDictionarybyNumber[33] = ["Maya Yukikaze",u"雪風真弥"]
    girlDictionarybyNumber[34] = ["Lee Chunyan",u"李春燕"]
    girlDictionarybyNumber[35] = ["Akira Hatori",u"羽鳥晶"]
    girlDictionarybyNumber[36] = ["Kira Hayashida",u"林田希羅"]
    girlDictionarybyNumber[37] = ["Mirei Ayanokoji",u"綾小路美麗"]
    girlDictionarybyNumber[38] = ["Eri Minaguchi",u"皆口英里"]
    girlDictionarybyNumber[39] = ["Hana Yamada",u"山田はな"]
    girlDictionarybyNumber[40] = ["Rui Takasaki",u"高崎瑠依"]
    girlDictionarybyNumber[41] = ["Hina Nigaki",u"新垣雛菜"]
    girlDictionarybyNumber[42] = ["Yukie Yatsuka",u"八束由紀恵"]
    girlDictionarybyNumber[43] = ["Akane Sakurai",u"櫻井明音"]
    girlDictionarybyNumber[44] = ["Kodama Yamano",u"山野こだま"]
    girlDictionarybyNumber[45] = ["Shiori Shiratori",u"白鳥詩織"]
    girlDictionarybyNumber[46] = ["Yulia Valkova",u"ユーリヤ・ヴャルコワ"]
    girlDictionarybyNumber[47] = ["Moeka Nitta",u"新田萌果"]
    girlDictionarybyNumber[48] = ["Nanase Minamida",u"南田七星"]
    girlDictionarybyNumber[49] = ["Mai Masaoka",u"正岡真衣"]
    girlDictionarybyNumber[50] = ["Akiho Shigeto",u"重藤秋穂"]
    girlDictionarybyNumber[51] = ["Nao Miyoshi",u"見吉奈央"]
    girlDictionarybyNumber[52] = ["Nagiko Kurokawa",u"黒川凪子"]
    girlDictionarybyNumber[53] = ["Chizuru Onodera",u"小野寺千鶴"]
    girlDictionarybyNumber[54] = ["Kazuha Kumada",u"熊田一葉"]
    girlDictionarybyNumber[55] = ["Sonomi Kakei",u"掛井園美"]
    girlDictionarybyNumber[56] = ["Mayuri Oyama",u"大山真由里"]
    girlDictionarybyNumber[57] = ["Remi Tamai",u"玉井麗巳"]
    girlDictionarybyNumber[58] = ["Nae Yuki",u"優木苗"]
    girlDictionarybyNumber[59] = ["Rei Shinonome",u"東雲レイ"]
    girlDictionarybyNumber[60] = ["Kise Yukawa",u"湯川基世"]
    girlDictionarybyNumber[61] = ["Ichigo Kohinata",u"小日向いちご"]
    girlDictionarybyNumber[62] = ["Miss Monochrome", u"ミス・モノクローム"]
    girlDictionarybyNumber[63] = ["Kinoko Himejima",u"姫島木乃子"]
    girlDictionarybyNumber[64] = ["Chloe Lemaire",u"クロエ・ルメール"]
    girlDictionarybyNumber[65] = ["Kokomi Shina",u"椎名心実"]
    girlDictionarybyNumber[66] = ["Yoko Tsukishiro",u"月白陽子"]
    girlDictionarybyNumber[67] = ["Fumio Murakami",u"村上文緒"]
    girlDictionarybyNumber[68] = ["Noriko Kiryu",u"霧生典子"]
    girlDictionarybyNumber[69] = ["Shuri Furuya",u"古谷朱里"]
    girlDictionarybyNumber[70] = ["Michiru Tomura",u"戸村美知留"]
    girlDictionarybyNumber[71] = ["Marika Saeki",u"佐伯鞠香"]
    girlDictionarybyNumber[72] = ["Haruko Yumesaki",u"夢前春瑚"]
    girlDictionarybyNumber[73] = ["Eiko Hibara",u"飛原鋭子"]
    girlDictionarybyNumber[74] = ["Isuzu Shiranui",u"不知火五十鈴"]
    girlDictionarybyNumber[75] = ["Erena Mochizuki",u"望月エレナ"]
    girlDictionarybyNumber[76] = ["Rino Suzukawa",u"鈴河凜乃"]
    girlDictionarybyNumber[77] = ["Nonoka Sasahara",u"笹原野々花"]
    girlDictionarybyNumber[78] = ["Saya Kagurazaka",u"神楽坂砂夜"]
    girlDictionarybyNumber[79] = ["Tsugumi Harumiya",u"春宮つぐみ"]
    girlDictionarybyNumber[80] = ["Raimu Nejikawa",u"螺子川来夢"]
    girlDictionarybyNumber[81] = ["Nozomi Miyauchi",u"宮内希"]
    girlDictionarybyNumber[82] = ["Yuki Kubota",u"久保田友季"]
    girlDictionarybyNumber[83] = ["Kaoru Arai",u"荒井薫"]
    girlDictionarybyNumber[84] = ["Yuri Otowa",u"音羽ユリ"]
    girlDictionarybyNumber[85] = ["Kei Asami",u"浅見景"]
    girlDictionarybyNumber[86] = ["Serina", u"芹那"]
    girlDictionarybyNumber[87] = ["Mayuko Yoshikawa",u"吉川繭子"]
    girlDictionarybyNumber[88] = ["Kaho Mishina",u"三科果歩"]
    girlDictionarybyNumber[92] = ["Kyoko Tachibana",u"橘響子"]
    girlDictionarybyNumber[93] = ["Kaede Yuge",u"弓削楓"]
    girlDictionarybyNumber[97] = ["Mutsumi Shigino",u"鴫野睦"]
    girlDictionarybyNumber[98] = ["Mei Morizono",u"森園芽以"]
    girlDictionarybyNumber[99] = ["Yuzuko Hazuki",u"葉月柚子"]
    girlDictionarybyNumber[100] = ["Shinobu Kokonoe",u"九重忍"]
    girlDictionarybyNumber[101] = ["Momoko Asahina",u"朝比奈桃子"]
    girlDictionarybyNumber[102] = ["Masako Hatayama",u"畑山政子"]
    girlDictionarybyNumber[103] = ["Matsuri Kagami",u"加賀美茉莉"]
    girlDictionarybyNumber[104] = ["Akari Amari",u"甘利燈"]
    girlDictionarybyNumber[109] = ["Isuki Ishida",u"石田いすき"]
    girlDictionarybyNumber[110] = ["Mahiro Natsume",u"夏目真尋"]
    girlDictionarybyNumber[111] = ["Kanata Amatsu",u"天都かなた"]
    girlDictionarybyNumber[112] = ["Saeko Arisugawa",u"有栖川小枝子"]
    girlDictionarybyNumber[113] = ["Satoru Kimijima",u"君嶋里琉"]
    girlDictionarybyNumber[115] = ["Koruri Tokitani",u"時谷小瑠璃"]
    girlDictionarybyNumber[116] = ["Yurara Mishima",u"三嶋ゆらら"]
    girlDictionarybyNumber[117] = ["Tomo Oshi",u"押井知"]
    girlDictionarybyNumber[119] = ["Tsuzuri Shirase",u"白瀬つづり"]
    girlDictionarybyNumber[120] = ["Haruka Kazemachi",u"風町陽歌"]
    girlDictionarybyNumber[121] = ["Emi Sagara",u"相楽エミ"]
    girlDictionarybyNumber[122] = ["Ayame Chiyoura",u"千代浦あやめ"]
    girlDictionarybyNumber[123] = ["Otome Kayashima",u"栢嶋乙女"]
    girlDictionarybyNumber[124] = ["Kazumi Kawabuchi",u"川淵一美"]
    girlDictionarybyNumber[125] = ["Ibuki Fukita",u"芙来田伊吹"]
    girlDictionarybyNumber[137] = ["Kanna Hashimoto", u"橋本環奈"]
    girlDictionarybyNumber[138] = ["Mimi Takeuchi",u"武内未美"]
    girlDictionarybyNumber[148] = ["Sumire Yomogida",u"蓬田菫"]
    girlDictionarybyNumber[156] = ["Risa Shinomiya",u"篠宮りさ"]
    girlDictionarybyNumber[164] = ["Shiki Nanami",u"七海四季"]
    girlDictionarybyNumber[166] = ["Chika Oribe",u"織部千華"]
    girlDictionarybyNumber[168] = ["Wakana Yoshinaga",u"吉永和花那"]
    girlDictionarybyNumber[172] = ["Yayoi Yutenji",u"祐天寺弥生"]
    girlDictionarybyNumber[176] = ["Ema Fukami",u"深見絵真"]
    girlDictionarybyNumber[179] = ["Yuki Hanafusa",u"花房優輝"]
    girlDictionarybyNumber[180] = ["Shirabe Narumi",u"鳴海調"]
    girlDictionarybyNumber[183] = ["Botan Sorimachi",u"反町牡丹"]
    girlDictionarybyNumber[184] = ["Asuka Ukihashi",u"浮橋明日香"]
    girlDictionarybyNumber[185] = ["Yu Naoe",u"直江悠"]
    girlDictionarybyNumber[194] = ["Kasuga Asato",u"朝門春日"]
    girlDictionarybyNumber[195] = ["Subaru Makise",u"牧瀬昴"]
    girlDictionarybyNumber[196] = ["Miyabi Kunishiro",u"久仁城雅"]
    girlDictionarybyNumber[199] = ["Shizuko Todo",u"藤堂静子"]
    girlDictionarybyNumber[200] = ["Toko Mashiro",u"真白透子"]
    girlDictionarybyNumber[202] = ["Hibiki Toyonaga",u"豊永日々喜"]
    girlDictionarybyNumber[203] = ["Anette Olga Karasawa",u"アネット・オルガ・唐澤"]
    girlDictionarybyNumber[204] = ["Yae Sanjo",u"三条八重"]
    girlDictionarybyNumber[208] = ["Sora Takara",u"高良美空"]
    girlDictionarybyNumber[209] = ["Umi Takara",u"高良美海"]
    girlDictionarybyNumber[212] = ["Madoka Kaname", u"鹿目まどか"]
    girlDictionarybyNumber[213] = ["Homura Akemi", u"暁美ほむら"]
    girlDictionarybyNumber[214] = ["Mami Tomoe", u"巴マミ"]
    girlDictionarybyNumber[215] = ["Sayaka Miki", u"美樹さやか"]
    girlDictionarybyNumber[216] = ["Kyouko Sakura", u"佐倉杏子"]
    girlDictionarybyNumber[217] = ["Hitomi Shizuki", u"志筑仁美"]
    girlDictionarybyNumber[219] = ["Cocoa", u"ココア"]
    girlDictionarybyNumber[220] = ["Chino", u"チノ"]
    girlDictionarybyNumber[221] = ["Rize", u"リゼ"]
    girlDictionarybyNumber[222] = ["Chiya", u"千夜"]
    girlDictionarybyNumber[223] = ["Sharo", u"シャロ"]
    def __init__(self):
        for i in range(225):
            self.start_urls.append("http://gfkari.gamedbs.jp/girl/detail/" + str(1 + i))

    def parse(self, response):
        urls = response.xpath("//section//a[@class='cl']/@href").extract()
        titles = response.xpath("//section//a[@class='cl']/@title").extract()
        for i in range(len(urls)):
            item = GfimagesItem()
            base = urls[i][13:]
            url = 'http://gfkari.gamedbs.jp' + urls[i]
            title = titles[i]
            request = scrapy.Request(url=url, callback=self.image_parser)
            start = title.find("No.") + 3
            end = title.find(" ")
            card_id = title[start:end]
            card_id.lstrip()
            if int(card_id) <= 8598:
                continue
            item['image_url'] = url
            item['thumbnail_url'] = 'http://gfkari.gamedbs.jp/images/card/icon/collection/' + base
            request.meta['card_id'] = card_id
            request.meta['item'] = item
            yield request

    def image_parser(self, response):
        item = response.meta['item']
        card_id = response.meta['card_id']
        # hash generation so people don't crawl my database
        # im salty that nobody has a easy-to-crawl db ok
        m = hashlib.md5()
        m.update(str(datetime.datetime.now()))
        image_name = m.hexdigest()
        item['card_id'] = card_id
        item['image_name'] = image_name
        yield item
