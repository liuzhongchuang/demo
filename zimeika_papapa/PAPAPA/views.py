import requests
from django.shortcuts import render

# Create your views here.
from lxml import etree


home_url = "https://zimeika.com"


def getMes(url):
    data = []
    res = requests.get(url)
    text_xml = etree.HTML(text=res.text)
    all_mes = text_xml.xpath('//form[@class="am-form"]//tbody/tr')
    for x in all_mes:
        feilei = x[0].text.replace('\xa0', '')
        tiltle = x[0].xpath('a/text()')[0]
        urls = home_url + x[0].xpath('a/@href')[0]
        author = x[1].xpath('a')[0].text
        time = x[2].text
        readNum = x[3].text
        commentNum = x[4].text
        data.append({feilei+tiltle+'-'+author+'-'+time+readNum+'-'+commentNum:urls})
    return data
def getContent(request,p):
    if '1' == p:
        print('11111')
        uc_url = 'https://zimeika.com/article/lists/uctoutiao.html'
        mes = getMes(uc_url)
    elif '2' == p:
        youxi_url = 'https://zimeika.com/article/lists/uctoutiao.html?cate_id=17'
        mes = getMes(youxi_url)
    elif '3' == p:
        junshi_url = 'https://zimeika.com/article/lists/uctoutiao.html?cate_id=16'
        mes = getMes(junshi_url)
    elif '4' == p:
        lishi_url = 'https://zimeika.com/article/lists/uctoutiao.html?cate_id=12'
        mes = getMes(lishi_url)
    elif '5' == p:
        jiankang_url = 'https://zimeika.com/article/lists/uctoutiao.html?cate_id=11'
        mes = getMes(jiankang_url)
    else:
        gaoxiao_url = 'https://zimeika.com/article/lists/uctoutiao.html?cate_id=9'
        mes = getMes(gaoxiao_url)
    print('777777')
    return render(request, 'base.html', {'data':mes})

def index(request):
    uc_url = 'https://zimeika.com/article/lists/uctoutiao.html'
    mes = getMes(uc_url)
    return render(request, 'base.html', {'data':mes})