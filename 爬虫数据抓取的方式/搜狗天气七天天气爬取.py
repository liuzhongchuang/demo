# @Time    : 2018/10/18 0018 08:52
# @Author  : lzc
# @File    : 搜狗天气七天天气爬取.py

import pymongo
import time
import requests
from pyquery import PyQuery as pq

client = pymongo.MongoClient(host='127.0.0.1')#主机地址的地址
mgdb = client.Qtianqi
coll = mgdb.qtianqi#设计数据库的表
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'
}#网页上返回的头包地址


def weatherdetail(url):
    res = requests.get(url, headers=header)
    # print(url)
    doc = pq(res.text)
    #详细信息是li的无序列表
    details = doc('ul.r-weather li')#类的名字（详细信息）最上层
    # print(details)
    data = {}
    for d in details.items():
        data={
             '具体日期': d.find('.wrapper').text(),
            # '天气状况': d.find('.wrapper des').text(),
            # '风力': d.find('.wrapper wind').text(),
            # '具体日期2': d.find('.wrapper.date').text(),
            # '天气状况2': d.find('.wrapper.des').text(),
            # '温度2': d.find('.wrapper.date').text(),

        }
        #查询房屋详细信息的地址
        # house_detail_url = d.find('a').attr('href')
        # print(house_detail_url)
        # coll.insert(data)
    print(data)

while True:
    url = 'http://tianqi.sogou.com/?tid=101280601'
    weatherdetail(url)
    time.sleep(5)
