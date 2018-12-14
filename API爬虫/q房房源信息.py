# @Time    : 2018/11/27 0027 10:28
# @Author  : lzc
# @File    : q房房源信息.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'
}
mes = []
def getHouseInfo(url):
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    h_info = soup.select('div#cycleListings li')
    for h in h_info:
        info = []
        title = h.select('.house-title a')[0].text
        info.append(title)
        detail = h.select('.house-about.clearfix')[0].text.split('|')
        detail2 = detail[0].strip()+'-'+detail[1].strip()+'-'+detail[2].strip()+'-'+detail[3].strip()+'-'+detail[4].strip()
        info.append(detail2)
        didian = h.select('.whole-line')[0].text.split('-')
        didian2 = ''
        for d in didian:
            didian2 = didian2+d.strip()+'-'
        info.append(didian2)
        fangzu = h.select('.show-price')[0].text.split()
        fangzu2 = fangzu[0]+fangzu[1]
        info.append(fangzu2)
        h_url = 'https://shenzhen.qfang.com'+h.select('a.show-image')[0].get('href')
        info.append(h_url)
        mes.append(info)
        # print('标题：', title)
        # print('详细：', detail2)
        # print('地点：', didian2)
        # print('房租：', fangzu2)
        # print('房源链接：', h_url)
    t = ['标题', '房子描述', '地点', '房租', '房源链接']
    cf = pd.DataFrame(mes, columns=t)#房子集合+表头
    cf.to_csv("housemes.csv", encoding="utf-8")#文件名+编码
    ex_first = pd.read_csv("housemes.csv", encoding="utf-8")
    print(ex_first)
for i in range(1,66):
    url = 'https://shenzhen.qfang.com/rent/f%d' % i
    time.sleep(3)
    getHouseInfo(url)