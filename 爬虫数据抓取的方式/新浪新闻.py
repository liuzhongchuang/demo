# @Time    : 2018/10/18 0018 15:53
# @Author  : lzc
# @File    : 新浪新闻.py
import time
from urllib import request

import pymongo
import requests
from bs4 import BeautifulSoup
import sys

client = pymongo.MongoClient(host='127.0.0.1')
mgdb = client.xinlang
coll = mgdb.xinwen

url ='https://news.sina.com.cn/society/'
def getnewsdetails(news_title,news_url):
    #另外的方法获取一个request对象
    res = request.Request(news_url)
    response = request.urlopen(res)
    #以上两步等于response = requests.get(url),不过下面的就不是.text而是.read()
    soup = BeautifulSoup(response.read(),'html.parser')

    #获取新闻内容
    tag = soup.select('#article')

    #获取新闻发布时间
    #第一种方法获取数据（标签加类的名称）
    # news_date = soup.find('div',class_='data-source').span.text

    # #第二种方法获取数据（省略class_）
    # news_date = soup.find('div','data-source').span.text
    # #第三种获取数据的方式（select）select取到的是一个集合所以需要取下标
    news_date = soup.select('.date-source')[0].text
    # print(news_date)
    # #第四种获取数据的方法把html的标签的名称放进去
    # news_date = soup.select('.div.date-source span')[0].text
    # #获取标签子目录下的a标签的内容
    news_source = soup.find('div',class_='date-source').a.text
    #将获取新闻发布的来源写入到文件中
    # filePathname = sys.path[0]+'/news/'+news_title+'.txt'
    # with open(filePathname, 'w',encoding='utf-8') as fl:
    #     fl.write(news_date+"    "+news_source+'\n')
    #     content = ''
    #     for p in tag:
    #         content = content+p.text
    #     print(content)
    #     fl.write(content)
    # print(news_date)

'''
获取评论数和参与人数
'''
def getcount(news_title,news_url):
    a = news_url.split('i')[-1].split('.')[0]
    # print(a)
    news_url2 = 'https://comment.sina.com.cn/page/info?version=1&f' \
                'ormat=json&channel=sh&newsid=comos-%s&group=undefined&com' \
                'press=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'% a
    rep = requests.get(news_url2)
    json1 = rep.json()
    if json1:
        comment = json1['result']['count']['show']
        allman = json1['result']['count']['total']
        print('新闻标题：%s'% news_title,'评论人数：%d'% comment,'参与人数：%d'%allman)



'获取新闻标题'
def getnewstitle(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    #转成DOM元素结构
    soup = BeautifulSoup(response.text,'html.parser')
    #获取新闻列表的两种方法
    news = soup.select('ul.news-2 li')#表示在ul标签里类名class=news-2他的下一级li标签的数据
    # news = soup.find('ul',calss_='news-2').find_all('li')
    #表里每一个li标签，标签li里都是a标签，获取url地址就是获取a标签的href对应属性值
    for li in news:
        news_title = li.a.text
        news_url = li.a.get('href')
        print(news_title,news_url)
        # getnewsdetails(news_title, news_url)
        getcount(news_title,news_url)
        time.sleep(2)

getnewstitle(url)







