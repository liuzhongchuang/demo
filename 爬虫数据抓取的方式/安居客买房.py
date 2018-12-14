# @Time    : 2018/10/17 0017 16:49
# @Author  : lzc
# @File    : 安居客买房.py
import pymongo
import time
import requests
from pyquery import PyQuery as pq

client = pymongo.MongoClient(host='127.0.0.1')
mgdb = client.anjuke
coll = mgdb.house
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'
}#网页上返回的头包地址


def HouseDetail(url):
    res = requests.get(url, headers=header)
    # print(url)
    doc = pq(res.text)
    #详细信息是li的无序列表
    details = doc('.list-item')#类的名字（详细信息）如li标签的类名它一般会有很多一样的
    data = {}
    for d in details.items():
        data={
            '房屋总价':d.find('.price-det').text(),
            '每平方米的价格':d.find('.unit-price').text(),
            '所在位置':d.find('.comm-address').text()
        }
        #查询房屋详细信息的地址
        house_detail_url = d.find('a').attr('href')
        # print(house_detail_url)
        # coll.insert(data)
        print(data)

for i in range(1,3):
    url = 'https://shenzhen.anjuke.com/sale/p{}/#filtersort'.format(i)
    HouseDetail(url)
    time.sleep(5)

