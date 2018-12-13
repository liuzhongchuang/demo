# @Time  :2018/11/6  9:32
# @Author:LongAt
# @File  :urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url('^list/(\d+)$', views.getContent),
    url('^$', views.index),
    ]