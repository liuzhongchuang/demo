# @Time :2018/9/19 001916:43
# @Author :Alex
# @File  :urls.py.py

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^$', views.add),

    url(r'^add/(\d+)/(\d+)/$', views.add, name='add'),
    url(r'^min/(\d+)/(\d+)/$', views.min, name='min'),
    url(r'^(?P<i_num>[0-9]+)/min/$', views.min),
    url(r'^add_to_min/(\d+)/(\d+)/$', views.add_to_min, name='add_to_min'),
    # url('^polls', include('polls.urls')),
]