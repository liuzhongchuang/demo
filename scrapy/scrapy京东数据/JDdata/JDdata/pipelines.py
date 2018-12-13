# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from JDdata.items import jdClassifyItem, goodsItem


class JddscPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        #指定数据库名
        db = client['JDDB']
        #指定表名
        self.jdClass = db['JdClassify']

     #往mongodb数据库里面增加数据
    def process_item(self,item,spider):
        self.jdClass.insert(dict(item))
        return item


class JdgoodPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        #指定数据库名
        db = client['JDgd']
        #指定表名
        self.jdgd = db['Jdgoodlist']
        self.jdgoods = db['Goods']

     #往mongodb数据库里面增加数据
    def process_item(self,item,spider):
        # 所有的item全部提交到这里来处理，所以需要对item做一个类别的判断 isinstance
        if isinstance(item, jdClassifyItem):
            self.jdgd.insert(dict(item))

        if isinstance(item, goodsItem):
            self.jdgoods.insert(dict(item))
