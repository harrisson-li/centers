# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CityItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    center = scrapy.Field()
    date = scrapy.Field()
    brand = scrapy.Field()
