# @Time    : 2018/11/13 0013 19:23
# @Author  : lzc
# @File    : 培训机构抓取.py
import time
import pymongo
import requests
from bs4 import BeautifulSoup
from lxml import etree
from scrapy import Selector
import pandas as pd
# client = pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
# mgdb = client.zhaopin
# coll = mgdb.xinxi
mes = []
def getcontent(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # 转成DOM元素结构
    soup = BeautifulSoup(response.text, 'html.parser')
    contents = soup.select('div.table-view-cap.job-list')
    for c in contents:
        gs = []
        # data = {}
        gongsi = c.text.split('/')[0]
        gs.append(gongsi)
        didian = '深圳'+c.text.split('/')[1]
        gs.append(didian)
        gangwei = c.text.split('/')[2]
        gs.append(gangwei)
        xueli = c.text.split('/')[3]
        gs.append(xueli)
        shijian = c.text.split('/')[-1]
        gs.append(shijian)
        mes.append(gs)
        # data = {'公司':gongsi,'地点':didian,'招聘职位类型':gangwei,'学历要求':xueli,'发布时间':shijian}
        # data = {'公司':gongsi}
    t = ['公司名称', '公司地址', '招聘岗位', '学历要求', '时间']
    dt = pd.DataFrame(mes, columns=t)#房子集合+表头
    dt.to_csv("zhaopin.csv", encoding="utf-8")#文件名+编码
    ex_first = pd.read_csv("zhaopin.csv", encoding="utf-8")
    print(ex_first)

        # coll.insert(data)

urls = [
    'http://shenzhen.baixing.com/laoshi/m37339/',
    'http://shenzhen.baixing.com/laoshi/m177819/',
    'http://shenzhen.baixing.com/laoshi/m37338/',
    'http://shenzhen.baixing.com/laoshi/m178670/',
    'http://shenzhen.baixing.com/laoshi/m37347/',
    'http://shenzhen.baixing.com/laoshi/m37340/',
    'http://shenzhen.baixing.com/laoshi/m183583/',
    'http://shenzhen.baixing.com/laoshi/m183578/',
]
for url in urls:
    time.sleep(2)
    getcontent(url)

