# @Time    : 2018/10/9 0009 14:54
# @Author  : lzc
# @File    : urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pay',views.pay),
    url(r'^$',views.place_order),
    url(r'^user_center_site.html',views.site),
    url(r'^addorder/$',views.addOrder)

]