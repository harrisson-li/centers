# -*- coding: utf-8 -*-
import scrapy
import time
import json
import win_unicode_console

from centers.items import CityItem

win_unicode_console.enable()


class WebiSpider(scrapy.Spider):
    name = 'webi'
    allowed_domains = ['webi.com.cn']
    start_urls = ['https://www.webi.com.cn/study']

    def parse(self, response):
        request_url_list = ["https://www.webi.com.cn/api/center_citys_list/b24d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/d04d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/e24d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/144e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ca4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/d24d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/e04d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/f64d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/104e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/044e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/084e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/d44d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/1e4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/3e3474fb-9c73-e411-80c2-000c297f722d",
                            "https://www.webi.com.cn/api/center_citys_list/204e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/d84d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ba4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/de4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ea4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/184e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/024e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/e44d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/f24d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/064e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/f04d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/dc4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/344e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c44d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/b84d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ce4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ec4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/d64d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/e84d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c84d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/be4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c04d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/2a4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/b64d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/f44d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/fe4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/0e4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/124e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c3ac560c-7619-e911-80f9-005056b61b55",
                            "https://www.webi.com.cn/api/center_citys_list/bc4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/004e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/cc4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c24d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/fa4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/2e4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/304e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/b44d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/e64d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/da4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/c64d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/ee4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/0a4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/1a4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/2c4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/324e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/fc4d822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/0c4e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/164e822b-8539-e411-80d6-000c2957ec4f",
                            "https://www.webi.com.cn/api/center_citys_list/1c4e822b-8539-e411-80d6-000c2957ec4f"
                            ]

        for url in request_url_list:
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        js = json.loads(response.body_as_unicode())

        city = CityItem()

        city['name'] = js['data'][0]['city_name']
        # print(city['name'])

        city['number'] = 0
        city['center'] = []

        for center in js['data']:
            # print(center['center_name'])
            if not (center['center_name'].__contains__('删') or center['center_name'].__contains__('停')):
                city['center'].append(center['center_name'])
                city['number'] = city['number'] + 1

        # print(city['number'])
        city['date'] = time.strftime("%Y-%m-%d")
        city['brand'] = 'webi'

        yield city
