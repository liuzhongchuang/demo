# @Time    : 2018/10/17 0017 10:39
# @Author  : lzc
# @File    : 搜狗天气.py
import time

import pymongo
from bs4 import BeautifulSoup

import requests

client = pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
mgdb = client.weather
coll = mgdb.tianqi

def getweather():
    #定义要抓取的url地址
    url = 'http://tianqi.sogou.com/?tid=101280601'
    response = requests.get(url)
    #将获取的内容转变成DOM元素结构
    soup = BeautifulSoup(response.text,'html.parser')
    wendu = soup.select('.num')[0].text
    # shidu = soup.find('span',class_='hundity').text
    shidu = soup.select('span.hundity')[0].text#标签+类名
    fengli = soup.select('.wind')[0].text
    tianqi = soup.select('.text')[0].text
    shijian = soup.select('.row2.row2-0 .date')[0].text


    weather = {
        '时间':shijian,
        '当前温度':wendu,
        '当前湿度':shidu,
        '当前风力':fengli,
        '天气':tianqi,

    }
    #向mongodb的表中增加数据
    # coll.insert(weather)
    print(weather)

while True:
    getweather()
    time.sleep(3)
