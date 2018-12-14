# @Time    : 2018/9/28 0028 16:33
# @Author  : lzc
# @File    : urls.py
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login_handle/$', views.login_handle),
    url(r'^login/$', views.login),
    url(r'^info/$', views.info),
    url(r'^site/$', views.site),
    url(r'^logout/$', views.logout),
    url(r'^user_center_order/$', views.user_center_order),
]