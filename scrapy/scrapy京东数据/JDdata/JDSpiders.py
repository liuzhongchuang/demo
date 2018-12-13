# @Time :2018/10/26 002614:48
# @Author :Alex
# @File  :JDSpiders.py
import re

import requests
from scrapy import Spider, Request, Selector, cmdline
from jdsc.items import jdClassifyItem, goodsItem

class JDSpiders(Spider):

    #定义蜘蛛名称
    name = 'JDSpider'

    # 价格连接地址
    price_url = 'https://c0.3.cn/stock?skuId=%s&cat=1320,1585,10975&venderId=1000008814&area=1_72_4137_0&buyNum=1&choseSuitSkuIds=&extraParam={"originid":"1"}&ch=1&fqsp=0&pduid=775011473'

    # 商品评论地址
    comment_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=%s'

    # 定义爬取京东的首页地址
    start_urls = [
        'https://www.jd.com/allSort.aspx'
    ]

    # 派发url到指定的parse去处理
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url = url,callback= self.parse_Classify_byReg)


    def parse_Classify(self, response):
        # 获取选择器
        selector = Selector(response)

        jd_contents = selector.xpath('//div[@class="items"]/dl/dd/a')

        for item in jd_contents:
            # 获取当前分类，也就是url地址的前面一部分，比如：下面的list表示可以获取分页数据，list之外的表示还有其他分类
            # //channel.jd.com/1713-3273.html
            # // list.jd.com / list.html?cat = 1713, 3274 & jth = i
            href = item.xpath('@href')[0].root
            name = item.xpath('text()')[0].root
            #当前url分类
            type = href.split('.')[0]
            #如果是//list开头，我们就构建item提交到数据库增加
            if type == '//list':
                jdClass = jdClassifyItem()
                #给item属性赋值
                jdClass['name']= name
                jdClass['url'] = href
                yield jdClass
            else:
                yield Request(url='https:'+href, callback=self.parse_Classify)

    # 使用正则表达式
    def parse_Classify_byReg(self, response):
        # 获取选择器
        selector = Selector(response)

        jd_contents = selector.xpath('//div[@class="items"]/dl/dd/a').extract()

        for item in jd_contents:
            # 获取当前分类，也就是url地址的前面一部分，比如：下面的list表示可以获取分页数据，list之外的表示还有其他分类
            # //channel.jd.com/1713-3273.html
            # // list.jd.com / list.html?cat = 1713, 3274 & jth = i

            #sRet接受一个和规则匹配的数组，比如下面就是href 和 a标签的显示内容
            sRet = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', item)
            for ret in sRet:
                #当前url分类
                type = ret[0].split('.')[0]
                #如果是//list开头，我们就构建item提交到数据库增加
                if type == '//list':
                    jdClass = jdClassifyItem()
                    #给item属性赋值
                    jdClass['name']= ret[1]
                    jdClass['url'] = ret[0]
                    # yield jdClass
                    yield Request(url='https:'+ret[0], callback=self.parse_Goods_List, meta={'classify':ret[1]})
                else:
                    yield Request(url='https:'+ret[0], callback=self.parse_Classify)


    # 通过分类点进列表界面，获取商品的相信信息的url地址
    def parse_Goods_List(self, response):
        selector = Selector(response)
        # 获取所有商品的url地址
        hrefs = selector.xpath('//div[@class="p-img"]/a/@href')
        for h in hrefs:
            # 进一步将商品地址分发到详细信息处理上去
            yield Request(url='https:'+h.root, callback=self.parse_Goods_Detail, meta= response.meta)


        #如果需要爬取多页
        next_page = selector.xpath('//a[@class="pn-next"]/@href').extract()
        if next_page:
            yield Request(url='https://list.jd.com'+next_page[0], callback=self.parse_Goods_List, meta=response.meta)


    # 在商品详细信息界面获取数据
    def parse_Goods_Detail(self, response):

        #构建一个商品对象item
        goods = goodsItem()
        goods['goodsName'] = response.xpath('//div[@class="sku-name"]/text()')[0].root.strip()
        goods['goodsUrl'] = response.url
        # goods['goodsUrl'] = response.xpath('//div[@class="sku-name"]/text()')
        goods['goodsId'] = response.url.split('/')[-1].split('.')[0]
        # 获取传过来的分类
        goods['goodsClassify'] = response.meta['classify']

        p_Url = 'https://c0.3.cn/stock?skuId=%s&cat=1320,1585,10975&venderId=1000008814&area=1_72_4137_0&buyNum=1&choseSuitSkuIds=&extraParam={"originid":"1"}&ch=1&fqsp=0&pduid=775011473'%goods['goodsId']
        # p_Url = self.price_url.format(goods['goodsId'])
        resp = requests.get(p_Url)
        resp = resp.json()

        goods['goodsPrice'] = resp['stock']['jdPrice']['p']


        p_Url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+ goods['goodsId']
        com_resp = requests.get(p_Url)
        com_resp = com_resp.json()
        goods['goodsCommentCount'] = com_resp['CommentsCount'][0]['CommentCountStr']
        goods['hp'] = com_resp['CommentsCount'][0]['GoodCountStr']
        goods['zp'] = com_resp['CommentsCount'][0]['GeneralCountStr']
        goods['cp'] = com_resp['CommentsCount'][0]['PoorCountStr']

        yield goods

cmdline.execute('scrapy crawl JDSpider'.split())