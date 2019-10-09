# -*- coding: utf-8 -*-
import scrapy
import time
import win_unicode_console

from centers.items import CityItem

win_unicode_console.enable()


class MeteniSpider(scrapy.Spider):
    name = 'meteni'
    allowed_domains = ['meteni.com']
    start_urls = ['http://www.meteni.com']

    def parse(self, response):

        page_links = []

        for i in range(1, 100):
            if i < 10:
                page_links.append('http://www.meteni.com/school_0{}.html'.format(i))
            else:
                page_links.append('http://www.meteni.com/school_{}.html'.format(i))

        for page in page_links:
            # print(page)
            yield scrapy.Request(page, callback=self.parse_item)

    def parse_item(self, response):
        items_1 = response.xpath("//div[@class='city fl']")
        items_2 = response.xpath("//ul[@class='fl']/li")

        for item1 in items_1:
            city = CityItem()
            city['name'] = item1.xpath("text()").extract()[0].rstrip(':')
            # print(city['name'])

            city['date'] = time.strftime("%Y-%m-%d")
            school_list = []

            for item2 in items_2:
                school = CityItem()
                school['name'] = item2.xpath("text()").extract()[0]
                if not (school['name'].__contains__('注册') or school['name'].__contains__('登录')):
                    school_list.append(school['name'])
                    # print(school['name'])

            city['number'] = len(school_list)
            city['center'] = school_list
            city['brand'] = 'meteni'
            yield city
