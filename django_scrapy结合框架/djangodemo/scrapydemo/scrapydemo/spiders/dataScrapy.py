# @Time    : 2018/11/12 0012 15:59
# @Author  : lzc
# @File    : dataScrapy.py
import requests
import scrapy
from scrapy import Selector, cmdline

from ..items import ScrapydemoItem
#这里是爬虫的代码这里的Item里面的定义的量名字都是在models里面的

class JDspider(scrapy.Spider):
    name = 'JDSpider'
    start_urls = [
        'https://www.jd.com/allSort.aspx'
    ]
    #派发url到指定的paese去处理
    def start_requests(self):
        for url in self.start_urls:#由上至下运行
            yield scrapy.Request(url=url,callback=self.parseclassify)

    def parseclassify(self, response):
        #获取选择器
        selector = Selector(response)
        jd_content = selector.xpath("//div[@class='items']/dl/dd/a")
        # print(jd_content)
        for item in jd_content:
            href = item.xpath('./@href')[0].root
            name = item.xpath('./text()')[0].root
            typel = href.split('.')[0]
            if typel == '//list':
                href1 = 'https:'+href
                yield scrapy.Request(url=href1,callback=self.getgood)

    def getgood(self, response):
        selector = Selector(response)
        goodlist = selector.xpath("//li[@class='gl-item']/div/div[@class='p-img']/a")
        for good in goodlist:
            goodlink = 'http:' + good.xpath("./@href")[0].root
            # print(goodlink)
            yield scrapy.Request(url=goodlink, callback=self.getgooddetail)

        # 如果爬取多页的话
        next_page = selector.xpath('//a[@class="pn-next"]/@href').extract()
        if next_page:
            yield scrapy.Request(url='https://list.jd.com' + next_page[0], callback=self.getgood)

    def getgooddetail(self, response):

        # urls = response.url
        # gid = urls.split('/')[-1].split('.')[0]
        # gcomnent_json_url = 'https://club.jd.com/comment/product' \
        #                     'CommentSummaries.action?referenceIds={}'.format(gid)
        # gprice = requests.get(gcomnent_json_url)
        # goodcom = gprice.json()
        # gooddt = BeautifulSoup(response.text,'html.parser')
        # print('好评数：',goodcom['CommentsCount'][0]['GoodCountStr'])
        #     print('差评数：',gcom['CommentsCount']['0']['PoorCountStr'])
        #     print('商品链接：',urls)
        # gpce = jdGoodItem()
        # gpce['price'] = goodprice['stock']['jdPrice']['p']
        # yield gpce
        # 构建一个商品对象item
        goods = ScrapydemoItem()
        goods['goodsName'] = response.xpath('//div[@class="sku-name"]/text()')[0].root
        goods['goodsUrl'] = response.url
        # goods['goodsUrl'] = response.xpath('//div[@class="sku-name"]/text()')
        goods['goodsId'] = response.url.split('/')[-1].split('.')[0]
        # 获取传过来的分类
        # goods['goodsClassify'] = response.meta['classify']

        p_Url = 'https://c0.3.cn/stock?skuId=%s&cat=1320,1585,10975&venderId=100000' \
                '8814&area=1_72_4137_0&buyNum=1&choseSuitSkuIds=&extraParam={"originid":"1"}&ch=1&f' \
                'qsp=0&pduid=775011473' % \
                goods['goodsId']
        # p_Url = self.price_url.format(goods['goodsId'])
        resp = requests.get(p_Url)
        resp = resp.json()

        goods['goodsPrice'] = resp['stock']['jdPrice']['p']

        p_Url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + goods['goodsId']
        com_resp = requests.get(p_Url)
        com_resp = com_resp.json()
        goods['goodsCommentCount'] = com_resp['CommentsCount'][0]['CommentCountStr']
        goods['hp'] = com_resp['CommentsCount'][0]['GoodCountStr']
        goods['zp'] = com_resp['CommentsCount'][0]['GeneralCountStr']
        goods['cp'] = com_resp['CommentsCount'][0]['PoorCountStr']
        yield goods

cmdline.execute('scrapy crawl JDSpider'.split())