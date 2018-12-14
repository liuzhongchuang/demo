from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from df_goods.models import GoodInfo
from df_order.models import OrderInfo
from df_user.models import UserInfo
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html', {'user': UserInfo.objects.all()})


def register_handle(request):
    if request.method == 'POST':
        u_user_name = request.POST.get('user_name')
        u_pwd = request.POST.get('pwd')
        u_email = request.POST.get('email')

    users = UserInfo(uname=u_user_name, upwd=u_pwd, uemail=u_email)
    users.save()
    # return render(request,'df_user/login.html', {'user': UserInfo.objects.all()})
    return HttpResponseRedirect('/user/login/') #重定向不要request


def register_exist(request):
    uname = request.GET.get('uname')
    #先做验证，验证用户是否在存在
    user = UserInfo.objects.filter(uname=uname)
    return HttpResponse(user.count())


def login(request):
    return render(request, 'df_user/login.html')


def login_handle(request):
    # return (request, 'df_goods/index.html',{'user': UserInfo.objects.all()})
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    user = UserInfo.objects.filter(uname=uname)
    if user.count() >= 1:
        if user[0].upwd == upwd:
            request.session['user_name'] = uname
            request.session['user_id'] = user[0].id
            return HttpResponseRedirect('/')
        else:
            return render(request, 'df_user/login.html', {'error_name': 0, 'error_pwd': 1})
    else:
        return render(request, 'df_user/login.html', {'error_name': 1, 'error_pwd': 0})
    # return render(request, 'df_goods/index.html')


def info(request):
    return render(request, 'df_user/user_center_info.html', {'goods_list': GoodInfo.objects.all()})


def user_center_order(request):
    return render(request, 'df_user/user_center_order.html', {'orderlist': OrderInfo.objects.all(), 'orderdetailinfo':OrderInfo.objects.all()})


def site(request):
    return render(request, 'df_user/user_center_site.html', {'user': UserInfo.objects.all()})


def logout(request):
    request.session.flush()
    # request.sessino['username'] = ''
    return HttpResponseRedirect('/')
    # return render(request, 'df_goods/index.html')
