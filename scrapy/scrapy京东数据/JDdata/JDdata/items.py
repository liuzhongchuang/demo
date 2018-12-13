# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item,Field
class JddataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class jdClassifyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


class goodsItem(scrapy.Item):
    goodsName = Field()  # 商品名称
    goodsUrl = Field()  # 商品链接
    goodsId = Field()  # 商品ID
    # goodsClassify = Field()  # 商品分类
    goodsPrice = Field()  # 商品价格
    goodsCommentCount = Field()  # 评论总数
    hp = Field()  # 好评
    zp = Field()  # 中评
    cp = Field()  # 差评
