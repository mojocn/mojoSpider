# -*- coding: utf-8 -*-

import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class W3CPipeline(object):
    def init(self):

        # 打开数据库连接
        db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        #cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        #data = cursor.fetchone()

        #print("Database version : %s " % data)

        # 关闭数据库连接
        #db.close()



        self.file = codecs.open('w3c.json', 'wb', encoding='utf-8')  # 打开文件

    def process_item(self, item, spider):
        line = json.dumps(item['title'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['link'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['desc'], ensure_ascii=False) + '\n'
        self.file.write(line)  # 写入文件
