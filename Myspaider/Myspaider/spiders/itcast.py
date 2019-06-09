# -*- coding: utf-8 -*-
import scrapy
from Myspaider.items import Itcast
import pymongo

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ('http://www.itcast.cn/channel/teacher.shtml#ajavaee',)

    def parse(self, response):
        filename = "teacher.html"
        # open(filename,'wb').write(response.body)
        items = []
        context = response.xpath("//div[@class='li_txt']")
        for text in context:
            # item = Itcast()
            item = {}
            name = text.xpath("h3/text()").extract()
            title = text.xpath("h4/text()").extract()
            info  = text.xpath('p/text()').extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            items.append(item)

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["itcast"]['teachers']
        x = mydb.insert_many(items)
        print(x.inserted_ids)