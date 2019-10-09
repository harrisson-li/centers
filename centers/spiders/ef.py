# -*- coding: utf-8 -*-
import scrapy
import time
import json
import win_unicode_console

from centers.items import CityItem

win_unicode_console.enable()


class EfSpider(scrapy.Spider):
    name = 'ef'
    allowed_domains = ['secure.englishtown.cn']
    start_urls = ['https://secure.englishtown.cn/']

    def parse(self, response):
        request_url_list = ["https://secure.englishtown.cn/online/cn/api/GetCentersByMarket?marketCode=cn&language=zh-cn"]

        for url in request_url_list:
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        js = json.loads(response.body_as_unicode())

        city = CityItem()

        for item in js['data']:
            city['name'] = item['CityName'] + item['AgeType']
            # print(city['name'])

            city['number'] = len(item['Schools'])
            # print(city['number'])
            city['center'] = []

            for center in item['Schools']:
                # print(center['Name'])
                city['center'].append(center['Name'])

            city['date'] = time.strftime("%Y-%m-%d")
            city['brand'] = 'ef'

            yield city

