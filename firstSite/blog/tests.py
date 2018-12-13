from datetime import date

from bs4 import BeautifulSoup
from django.test import TestCase
#coding:utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstSite.settings'

import django
django.setup()

from itertools import chain

from blog.models import Author, Blog, Department, Person

x = [1,2,3]
y = [4,5,{'a':12,'b':20}]
z = [6,7]

# 使用+将三个集合组合到一起
# aItems = x + y + z

# 使用chain函数
# aItems = chain(x, y, z)
#
# for a in aItems:
#     print(a)
#
#
#
# blog1 = (Blog.objects.filter(author_id=1))
# blog2 = (Blog.objects.filter(author_id=2))
#
# blogs = chain(blog1, blog2)
# # blogs = blog2 | blog1
# for x in blogs:
#     print(x)

#原生态方法一
# dept = Department()
# dept.name = '财务部'
# dept.create_date = date(2018,9,26)
# dept.save()

#原生态方法二
# dept = Department(name='开发部', create_date=date(2018,9,25))
# dept.save()

#调用默认管理器objects里面的create方法
# Department.objects.create(name='测试部', create_date=date(2018,9,25))

# 调用自定义管理器的creat_dept方法
# Department.operate_Dept.creat_dept(name='运营部', create_date=date(2018,9,25))

#调用自定义管理器的getDeptById方法
# depts = Department.operate_Dept.getDeptById('运')

# print(depts)

# per = Person()
# per.name = '小红'
# per.sex = '1'
# per.save()
#
# print(per.get_sex_display())


# -*- coding:UTF-8 -*-
 
import requests
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', class_ = 'showtxt')
     print(texts)