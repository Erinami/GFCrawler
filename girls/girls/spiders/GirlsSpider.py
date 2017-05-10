# -*- coding: utf8 -*-
# GFKARI GIRL CRAWLER
# Version 1.0 - yes, it's working how I need it to for now
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
from girls.items import GirlsItem

class GirlsSpider(scrapy.Spider):
    name = "girls"
    allowed_domains = ["ameba.jp", "gfkari.com", "gamedbs.jp"]
    start_urls = []
    girlid = 62
    girlsHit = 0;
    item = GirlsItem()

    def __init__(self):
        for i in range(1):
            self.start_urls.append("http://vcard.ameba.jp/s/api")

    def parse(self, response):
        for i in range(1): # for all girls of ID girlid to the range specified
            # make a request to crawl that girl, increment the girlid, then yield that request
            request = self.parseSub(response)
            self.girlid = self.girlid + 1
            yield request

    def parseSub(self, response):
        # let's crawl ameba's girl api endpoint. It's a post with the specified information. All of those cookies below are needed for authentication - well - at least some of them are needed
        # TODO: remove unnecessary cookies
        request = scrapy.FormRequest("http://vcard.ameba.jp/s/api", callback=self.parse_girls, method='POST', formdata={'apis':"[{\"key\":\"girl\",\"api\":\"directory/get\",\"data\":{\"profileId\":\"" + str(self.girlid) + "\"}}]"})

        # You'll need to put your cookies below here as a dictionary. I've included a few sample ones below.
        # Make sure that the cookies below are NOT EVER COMMITTED TO GITHUB ELSE SOMEONE COULD JUST LOG IN STRAIGHT INTO YOUR ACCOUNT OK
        request.cookies['deck-sort']='capability-desc'
        request.cookies['subDeck-sort']='capability-desc'
        request.cookies['ring-popup']='true'
        # put the rest of them here... just copy paste all the cookies from your browser when you're in the game

        # You need to have a CHROME HEADER. Otherwise, ameba will tell you to leave and redirect you to the opening PC splash screen NO MATTER WHAT YOU DO
        request.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

        # parse the request, so we go to the callback method specified (the one right below this line)
        return request

    def parse_girls(self, response):
        # If it's an error, we just yield absolutely nothing. because there was N O T H I N G
        # For some ridiculous reason, ameba's girl ids are scattered all over the place (probably to do with the fact that dual/triple/multiple-girl cards take up an girl id themself)
        if "message" in response.text:
            yield None

        # otherwise, lets make a girl item and load up the response json
        item = GirlsItem()
        locations = response.text
        variable = json.loads(locations)
        url = response.url

        # Response json has a girl array that contains all the information of the girl
        # Everything's hardcoded below because sublime text + quick text editing was easier than trying to figure out name differences and stuff
        # The japanese really don't know english do they
        item["cv"] = variable["girl"]["actorName"]
        item["cv_eng"] = variable["girl"]["actorName"]

        # Special case for age: need to remove the japanese character for "himitsu" with -1
        # Will then handle in front-end to display all negative ages as "Secret"
        # This is for data-type consistency in the db, so sorting by ages won't break
        age = variable["girl"]["age"]
        age = age.replace(u"秘", "-1")
        item["age"] = age[:-1]

        # special case for birthday: need to replace the japanese character for month and day with modern international standards
        # dates are still formatted as MM/DD/YYYY. Not sure if we should keep doing this or switch to international DD/MM/YYYY standard
        # but hey, it's america, and we can proably easily just batch-fix these in google sheets if we needed to, or even mysql idk
        # girls don't have a birth year (for obvious reasons). adding "2000 - age" for their year (1970 if unknown as unknowns are mostly teachers) so sorting works
        # but that just seems honestly weird. maybe there's a better way to do this, who knows
        birthday = variable["girl"]["birthday"]
        birthday = birthday.replace(u"\u6708", "/")
        birthday = birthday.replace(u"\u65e5", "")
        try:
            year = 2000 - int(item["age"])
        except ValueError:
            year = 1970
        if year > 1995:
            year = 1970
        birthday = birthday + "/" + str(year)
        item["birthday"] = birthday
        blood = variable["girl"]["blood"]
        item["blood"] = blood[:-1]
        item["bust"] = variable["girl"]["bust"]

        # oh great, classname has kanji in it
        # i'm just gonna flat out remove the kanji and hope that's enough for it to works
        # a girl with class 3 YEAR B CLASS will now just be 3B
        # if a girl has some other kanji in the class name, we'll have to manually edit it later because EXCEPTIONS
        # BOY DON'T WE LOVE EDGE CASES
        className = variable["girl"]["className"]
        className = className.replace(u"\u5e74", "")
        className = className.replace(u"\u7d44", "")
        item["className"] = className
        item["club"] = variable["girl"]["club"]
        item["club_eng"] = variable["girl"]["club"]
        item["description"] = variable["girl"]["description"]
        item["description_eng"] = variable["girl"]["description"]
        item["favorite_food"] = variable["girl"]["favoriteFood"]
        item["favorite_food_eng"] = variable["girl"]["favoriteFood"]
        item["year"] = variable["girl"]["grade"]
        item["hated_food"] = variable["girl"]["hateFood"]
        item["hated_food_eng"] = variable["girl"]["hateFood"]
        item["height"] = variable["girl"]["height"]
        item["hip"] = variable["girl"]["hip"]
        item["hobby"] = variable["girl"]["hobby"]
        item["hobby_eng"] = variable["girl"]["hobby"]
        item["girl_id"] = variable["girl"]["id"]
        item["name_hiragana"] = variable["girl"]["japaneseName"]
        item["name"] = variable["girl"]["name"]
        # do proper capitalization with the girl's english names
        englishName = variable["girl"]["alphabetName"].lower()
        item["name_eng"] = englishName.title()
        item["nickname"] = variable["girl"]["nickname"]
        item["nickname_eng"] = variable["girl"]["nickname"]
        item["horoscope"] = variable["girl"]["star"]
        item["horoscope_eng"] = variable["girl"]["star"]
        item["tweetName"] = variable["girl"]["tweetName"]
        item["waist"] = variable["girl"]["waist"]
        item["weight"] = variable["girl"]["weight"]
        item["translated"] = 0
        item["priority"] = 3

        # debugging purposes, as of 6/26/2016 there are 135 total girls in the game
        # but only 1 true waifu
        self.girlsHit = self.girlsHit + 1
        print "NUMBER OF GIRLS SO FAR"
        print self.girlsHit

        # replace the weird spacing in some of the english names
        url = item["name_eng"]
        url.replace(" ", "_", 1)
        url.replace(" ", "")
        item["name_eng"] = item["name_eng"].replace(u"\u3000", " ")

        # two special cases where ameba truly and really screwed up hard
        if item["girl_id"] == 204:
            url = "Yae_Sanjo"
            item["name_eng"] = "Yae Sanjo" # proper romanization would indeed be "Sanjyo", but the card says Sanjo on it. So until this gets fixed, we're leaving this as Sanjo
        if item["girl_id"] == 164:
            url = "Shiki_Nanami"
            item["name_eng"] = "Shiki Nanami" # ameba romanized the name in the wrong order. thanks.

        # now we're gonna crawl the english wiki because that already has some of the translated information. saves work.
        url = "https://wiki.gfkari.com/wiki/" + url
        request = scrapy.Request(url=url, callback=self.parse_wiki)
        request.meta['item'] = item # store the item in the metadata so we still have access to it
        yield request

    def parse_wiki(self, response):
        # we can get the item out from the metadata - as we stored it in there when we passed it here
        item = response.meta['item']

        # time for xpaths. who doesn't like xpaths?
        # look them up if you're not familiar with them. not gonna bother to comment this stuff.
        girlType = response.xpath('//th[contains(text(), "Type")]/../td/a/text()').extract()
        item['girlType'] = girlType[0]
        school = response.xpath('//th[contains(text(), "School")]/../td/a/text()').extract()
        item['school_eng'] = school[0]
        item['authority'] = response.xpath('//th[contains(text(), "Authority")]/../td/a/text()').extract()[0]
        item['horoscope'] = response.xpath('//th[contains(text(), "Horoscope")]/../td/a/text()').extract()[0]
        item['favorite_subject_eng'] = response.xpath('//th[contains(text(), "Subject")]/../td/text()').extract()[0].replace('\n', '')
        item['club_eng'] = response.xpath('//th[contains(text(), "Extracu")]/../td/a/text()').extract()[0]
        item['hobby_eng'] = response.xpath('//th[contains(text(), "Hobbies")]/../td/text()').extract()[0].replace('\n', '')
        item['favorite_food_eng'] = response.xpath('//th[contains(text(), "Favorite Food")]/../td/a/text()').extract()[0]
        item['hated_food_eng'] = response.xpath('//th[contains(text(), "Hated Food")]/../td/a/text()').extract()[0]
        item['cv_eng'] = response.xpath('//th[contains(text(), "CV")]/../td/a/text()').extract()[0]


        url = item['girl_id']

        # now for SOME REASON we're missing favorite subject information on the girls. so now it's time to crawl another damn site
        url = "http://gfkari.gamedbs.jp/girl/detail/" + str(url)
        request = scrapy.Request(url=url, callback=self.parse_gamedb)
        request.meta['item'] = item
        yield request

    def parse_gamedb(self, response):
        item = response.meta['item']
        # do the xpath, we gotta search for kanji so put it in unicode first
        # once we find it, gotta strip both sides of weird spaces in new lines because the formatting on this site is pretty wack
        school = u"\u5b66\u5712"
        favsubject = u"\u5f97\u610f\u79d1\u76ee"
        item['school'] = response.xpath('//th[contains(text(), "' + school + '")]/../td/text()').extract()[0]
        favsubtext = response.xpath('//th[contains(text(), "' + favsubject + '")]/../td/text()').extract()[0]
        favsubtext = favsubtext.replace('"', "")
        favsubtext = favsubtext.lstrip("\n")
        favsubtext = favsubtext.lstrip(" ")
        favsubtext = favsubtext.rstrip(" ")
        item['favorite_subject'] = favsubtext

        # yield the girl, aaaand we're done
        yield item


        # now finally, you're still not done. check the csv and make sure there are (as of june 2016) 135 girls.
        # check and make sure that there is no discrepency between japanese fields and english fields - make sure that there is no case where one is blank and the other is filled
        # check all new fields that have ??? or --- or are blank and make sure that is supposed to be the case
