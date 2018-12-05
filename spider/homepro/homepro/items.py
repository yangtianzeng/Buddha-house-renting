# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class HomeproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    title = scrapy.Field()  # 名字
    price = scrapy.Field()
    paytype = scrapy.Field()
    renttype = scrapy.Field()
    hometype = scrapy.Field()
    area  = scrapy.Field()
    decorade = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
    linkman = scrapy.Field()
    phone = scrapy.Field()
    img = scrapy.Field()
    features = scrapy.Field()


