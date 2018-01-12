# -*- coding: utf-8 -*-

import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from qiniu import Auth
from qiniu import BucketManager


class QiniuPipline(object):
    def __int__(self):
        access_key = '...'
        secret_key = '...'
        q = Auth(access_key, secret_key)
        self.bucket = BucketManager(q)

    def fetchOssImageByUrl(self, url, key):
        bucket_name = 'Bucket_Name'
        ret, info = self.bucket.fetch(url, bucket_name, key)
        print(info)
        assert ret['key'] == key

    def process_item(self, item, spider):
        self.bucket
        self.fetchOssImageByUrl('http://www.baidu.com', 'random-key')


class ZimuzuPipeline(object):
    def __init__(self):
        # 打开数据库连接
        # db = pymysql.connect("www.trytv.cn", "999", "8888", "trytv")

        # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        # cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()

        # print("Database version : %s " % data)

        # 关闭数据库连接
        # db.close()

        self.file = codecs.open('w3c.json', 'wb', encoding='utf-8')  # 打开文件

    def process_item(self, item, spider):
        line = json.dumps(item['title'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['link'], ensure_ascii=False) + '\t'
        line = line + json.dumps(item['desc'], ensure_ascii=False) + '\n'
        self.file.write(line)  # 写入文件
