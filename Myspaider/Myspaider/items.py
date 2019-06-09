# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspaiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Itcast(scrapy.Item):
	name = scrapy.Field()
	title = scrapy.Field()
	info = scrapy.Field()


class LgjobItem(scrapy.Item):
	companyfullname = scrapy.Field()
	positionname = scrapy.Field()
	salary = scrapy.Field()
	workyear = scrapy.Field()
	education = scrapy.Field()
	city = scrapy.Field()
	district = scrapy.Field()
	financestage = scrapy.Field()
	industryfield = scrapy.Field()
	firsttype = scrapy.Field()
	positionlables = scrapy.Field()