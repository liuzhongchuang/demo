from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse('我是第一个url测试')


def add(request, a, b):
    return HttpResponse('我做了增加操作'+a+'+'+b +'='+str(int(a)+int(b)))

'''
减法函数
'''
def min(request, a, b):
    return HttpResponse('我做了重定向到减法操作' + a + '-' + b + '=' + str(int(a) - int(b)))

"""
本来最初做加法，使用重定向函数，改向做减法，不改变url的路由配置和模版的url配置
"""
def add_to_min(request, a, b):
    return HttpResponseRedirect(
        reverse('min', args=(a, b))
    )