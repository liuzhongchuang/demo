from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from df_cart.models import CartInfo
from df_goods.models import GoodInfo
from df_order.models import OrderInfo,OrderDetailInfo
from df_user.models import UserInfo


def pay(request):
    return render(request, 'df_order/pay.html')


def place_order(request):
    # orderi = request.POST.get('orderid')
    # userid = request.session['user_id']
    # orderid = OrderInfo.objects.filter(user_id=userid)
    #先从参数里面获取所有的id
    orderids = request.GET.getlist('orderid')
    #这里需要根据前端传入的id来查，不能根据用户id
    orders = []
    for oid in orderids:
        orders.append(CartInfo.objects.get(id=oid))
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=user_id)

    # orderid = OrderInfo.objects.filter(id=orderid)
    return render(request, 'df_order/place_order.html',{'orderlist':orders,'user':user})


def site(request):
    # uname = request.POST.get('ushou')
    # uaddress = request.POST.get('uadress')
    # uyoubian = request.POST.get('uyoubian')
    # uphone = request.POST.get('uphone')
    # userinfo = UserInfo()
    # userinfo.ushou = uname
    return render(request,'df_user/user_center_site.html')


def addOrder(request):#先获取下单的所有购物车的id
    orderids = request.session.get('orderids')
    #构建一个订单对象
    order = OrderInfo()
    #查询订单最大的id
    oOder = OrderInfo.objects.all().order_by('oid')[0:1]
    if len(oOder) == 0:
        order.oid = 1
    else:
        print(int(oOder[0].oid))
        order.oid = int(oOder[0].oid)+1
    #增加订单时间
    order.odate = datetime.now()
    #是否付款
    order.oIsPay =0
    order.ototal=request.POST.get('totle')
    order.oaddress= request.POST.get('address')
    order.user_id= request.session.get('user_id')
    order.zhifu= request.POST.get('zhifu')
    order.save()
    #增加订单明细的商品洗信息
    for oid in orderids:#获取购物车（会有多条数据）
        cartInfo = CartInfo.objects.get(id=oid)
        good = GoodInfo.objects.get(id=cartInfo.goods_id)
        #如果返回2表示库存不够
        if cartInfo.count>good.gkucun:
            return JsonResponse({'status':2})

        #定义一个明细订单
        detail = OrderDetailInfo()
        detail.price = good.gprice
        detail.count = cartInfo.count
        detail.goods_id = good.id
        detail.price = order.oid
        detail.save()
        #如果返回1表示增加成功
    return JsonResponse({'status':1})