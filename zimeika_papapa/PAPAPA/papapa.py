# # @Time  :2018/11/5  15:19
# # @Author:LongAt
# # @File  :papapa.py
# from lxml import etree
# import scrapy
# import requests
# from scrapy import *
# from scrapy import cmdline
#
# home_url = 'https://zimeika.com'
#
# uc_url = 'https://zimeika.com/article/lists/uctoutiao.html'
#
# page_url = []
# for i in range(1, 11):
#     u_url = 'https://zimeika.com/article/lists/uctoutiao.html?p={}'.format(i)
#     page_url.append(u_url)
#
# # res = requests.get(url)
# # res.encoding = 'utf-8'
#
# dic = {}
# class zimeika(scrapy.Spider):
#     name = 'papapa'
#     def start_requests(self):
#         start_url = page_url
#         for u in start_url:
#             yield Request(url=u, callback=self.parse)
#
#     def parse(self, response):
#         text_xml = etree.HTML(text=response.body)
#         # text_xml = Selector(res)
#         all_mes = text_xml.xpath('//form[@class="am-form"]//tbody/tr')
#         # print(all_mes)
#         for x in all_mes:
#             feilei = x[0].text.replace('\xa0', '')
#             tiltle = x[0].xpath('a/text()')[0]
#             urls = home_url + x[0].xpath('a/@href')[0]
#             author = x[1].xpath('a')[0].text
#             time = x[2].text
#             readNum = x[3].text
#             commentNum = x[4].text
#             dic[tiltle] = [feilei, urls, author, time, readNum, commentNum]
#             print(dic)
#
# cmdline.execute('scrapy runspider papapa.py'.split())

