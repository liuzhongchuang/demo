# @Time    : 2018/10/24 0024 17:10
# @Author  : lzc
# @File    : 利用json抓取数据.py.py
import time

import requests
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
url = 'https://comment.sina.com.cn/page/info?version=1&format=json&channel=sh&newsid=comos-fxeuwws7735027&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
#从url地址获取数据
def getClickCount(url):
    res = requests.get(url)
    #判断是否获取数据成功

    json_data = res.json()
    # print(json_data)
    count = {}
    count['评论人数'] = json_data['result']['count']['show']
    print(count)

#.get('result').get('count')
x = 0
while x<3:
    getClickCount(url)
    x+=1
    # time.sleep(3)




