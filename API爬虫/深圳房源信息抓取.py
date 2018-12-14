# @Time    : 2018/11/26 0026 16:09
# @Author  : lzc
# @File    : 深圳房源信息抓取.py


import codecs
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import csv
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'
}
houseinfos = []
def getHouseInfo(url):
    res = requests.get(url,headers=header)
    soup = BeautifulSoup(res.text,'html.parser')
    house_mes = soup.select('div.r_lbx')

    for h in house_mes:
        houseinfo = []
        hinfo = h.select('.r_lbx_cena a')[0].text.strip()
        houseinfo.append(hinfo)
        hdetail = h.select('.r_lbx_cenb ')[0].text.split('|')
        hdetail2 = hdetail[0].strip()+'_'+hdetail[1].strip()+'_'+hdetail[2].strip()+'_'+hdetail[3].strip()+'租'
        houseinfo.append(hdetail2)
        money = h.select('span.ty_b')[0].text.strip()
        houseinfo.append(money)
        h_url = h.select('.r_lbx_cena a')[0].get('href')
        houseinfo.append(h_url)
        print('房子地点：',  hinfo)
        print('房子描述：', hdetail2)
        print('房源链接：', h_url)
        print('房租/月：', money)
        # houseinfos.append(houseinfo)

    # t = ['房子地点', '房子描述', '房租/月', '房源链接']
    # dt = pd.DataFrame(houseinfos, columns=t)#房子集合+表头
    # dt.to_csv("houseinfo.csv", encoding="utf-8")#文件名+编码
    # ex_first = pd.read_csv("houseinfo.csv", encoding="utf-8")
    # print(ex_first)
for i in range(1,3):
    url = 'https://www.dankegongyu.com/room/sz/w.html?page=%d' % i
    getHouseInfo(url)
    time.sleep(1)

