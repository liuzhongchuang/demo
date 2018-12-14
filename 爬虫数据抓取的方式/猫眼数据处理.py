# @Time    : 2018/10/16 0016 16:01
# @Author  : lzc
# @File    : 猫眼数据处理.py
import time

import requests
url = 'https://box.maoyan.com/promovie/api/box/second.json'
#从url地址获取数据
def getfilmdata():
    res = requests.get(url)

    #判断是否获取数据成功
    if res.status_code==200:
        json_data = res.json()
    else:
        print('获取数据失败')

    if json_data:  #从电影票房数据（json对象）中获取所有电影票房集合信息
        films = json_data.get('data').get('list')
        for item in films:
            film = {}
            film['影片名'] = item.get('movieName')
            film['上映天数'] = item.get('releaseInfo')
            film['总票房'] = item.get('movieName')
            film['综合票房'] = item.get('sumBoxInfo')
            film['票房占比'] = item.get('boxInfo')
            film['排片场次'] = item.get('boxRate')
            film['排片占比'] = item.get('avgShowView')
            film['场均人次'] = item.get('avgSeatView')
            print(film)

while True:
    getfilmdata()
    time.sleep(3)