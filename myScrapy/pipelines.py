# -*- coding: utf-8 -*-

import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class W3CPipeline(object):
    def init(self):
        self.file = codecs.open('w3c.json', 'wb', encoding='utf-8')  # 打开文件

    def process_item(self, item, spider):
        line = json.dumps(item['title'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['link'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['desc'], ensure_ascii=False) + '\n'
        self.file.write(line)  # 写入文件
