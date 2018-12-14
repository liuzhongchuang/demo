# @Time    : 2018/9/28 0028 16:18
# @Author  : lzc
# @File    : urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete/(\d+)/$', views.delete),
]
