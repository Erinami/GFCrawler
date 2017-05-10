# GFCrawler
Web crawler to obtain information on game objects in gfkari.

This python script uses scrapy to create a web crawler that obtains currently available information on the game objects from Girlfriend Kari. It hits a variety of sites including the game itself (ameba), the Japanese wiki, and the English wiki. Images are also handled, and renamed to a random hash. This table is also provided.

All of the returned tables need to be modified in Excel or some other CSV editor before it can be used in a database. Some of the sources that we are pulling data from provide occasional incorrect information (such as accidental misdirects), thus these need to be checked. The crawler will flag some of these values that are likely incorrect.

Stat generation is likely completely flawed due to how gamy's stat information appears to be completely wrong. Base and BaseMAX stats must be obtained by crawling the game site of a user that has obtained the card before. Luckily, a lot of cards seem to follow the same pattern, so this may be fixed in the near future.

Ribbon cards/Prism cards/Cards part of a set larger than 3: I have no clue how stat calculation works for them. Please contact me if you know how this works. 

To use the crawler, you need to include the cookies necessary for login in order for the site scraping the work correctly.
