# @Time    : 2018/9/29 0029 10:16
# @Author  : lzc
# @File    : urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^base/$', views.base),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^(\d+)/$', views.detail),
    url(r'^search/$', views.search),
    # url(r'^(?P<gi>\d+)/$', views.detail),
    # url(r'index/$', views.index),
]