from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from df_cart.models import CartInfo


def cart(request):
    #先获取用户ID
    userId = request.session['user_id']
    #根据用户信息查询他的购物车信息
    carts = CartInfo.objects.filter(user_id=userId)
    return render(request, 'df_cart/cart.html',{'carts':carts,'len':len(carts)})



def iflogin(func):
    def login(request,*args,**kwargs):#如果用户存在，执行调用的函数
        if request.session['user_id']:
            return func(request,*args,**kwargs)
        else:
            resp = HttpResponseRedirect('/user/login/')
    return login


@iflogin
def add(request,goodid,goodcount):
    #先获取用户id
    userId = request.session['user_id']
    #先验证购物车里面是否存在相同的产品
    Carts = CartInfo.objects.filter(user_id=userId).filter(goods_id=goodid)
    if len(Carts)>0:
        cart = Carts[0]
        cart.count +=int(goodcount)
    else:#定义一个购物车
        cart = CartInfo()
        cart.user_id = userId
        cart.goods_id = goodid
        cart.count = goodcount
    #保存购物车信息
    cart.save()
    #根据用户查询他的购物车信息
    carts = CartInfo.objects.filter(user_id=userId)
    return render(request,'df_cart/cart.html',{'carts':carts, 'len':len(carts)})


def edit(request):
    pass


def delete(request,goodid):
    cart = CartInfo()
    cart.id = goodid
    count = CartInfo.delete(cart)

    return JsonResponse({'date':'ok'})