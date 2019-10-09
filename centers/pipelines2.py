# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import time


class CentersPipeline(object):
    def process_item(self, item, spider):
        file_name = 'school_number_{}.csv'.format(time.strftime("%Y-%m-%d"))

        with open(file_name, 'a', newline='') as fp:
            data = [item['date'], item['brand'], item['name'], item['number'], item['center']]
            writer = csv.writer(fp)
            writer.writerow(data)

