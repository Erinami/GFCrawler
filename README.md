# GFCrawler
Web crawler to obtain information on game objects in gfkari.

This python script uses scrapy to create a web crawler that obtains currently available information on the game objects from Girlfriend Kari. It hits a variety of sites including the game itself (ameba), the Japanese wiki, and the English wiki. Images are also handled, and renamed to a random hash. This table is also provided.

All of the returned tables need to be modified in Excel or some other CSV editor before it can be used in a database. Some of the sources that we are pulling data from provide occasional incorrect information (such as accidental misdirects), thus these need to be checked. The crawler will flag some of these values that are likely incorrect.

Stat generation is likely completely flawed due to how gamy's stat information appears to be completely wrong. Base and BaseMAX stats must be obtained by crawling the game site of a user that has obtained the card before. Luckily, a lot of cards seem to follow the same pattern, so this may be fixed in the near future.

Ribbon cards/Prism cards/Cards part of a set larger than 3: I have no clue how stat calculation works for them. Please contact me if you know how this works. 

To use the crawler, you need to include the cookies necessary for login in order for the site scraping the work correctly.

EDIT 5/10/2017: gamy seems to no longer be updating their site with new cards. Their last updated card was #8598, and are missing roughly 12 cards between 8400 and 8598 that had to be manually added. The gfkari crawler, thus, is now outdated. A new version focusing on crawling data from gamedb and a few other select sources is in development, but due to the lack of information on these sites, the cards will have less pre-populated info.

EDIT 7/17/2017: Still looking for translators willing to help translate some of the descriptions of the cards if possible - any help would be greatly appreciated! A helper tool for obtaining information (including full stats information) on all cards a user has is also in development, but would require login credentials/cookie tokens. This may be the closest thing to fully-automated statistics population, but will likely not be used by many...
