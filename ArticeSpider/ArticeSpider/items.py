# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticeInfo(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()
    articedetail = scrapy.Field()
    print(1111111111111111)
    print(articedetail)
    print(222222222222222)
    pass

class ArticeDetial(scrapy.Item):

    pass