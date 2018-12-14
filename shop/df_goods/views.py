from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from df_goods.models import GoodInfo


def base(request):
    return render(request, 'df_goods/base.html')


def list(request, typeid,pageid,sortid):
    goodList=GoodInfo.objects.filter(gtype_id=typeid)
    #按照价格排序
    if sortid == '2':
        goodList = goodList.order_by('gprice')
    if sortid == '3':
        goodList = goodList.order_by('-gclick')
    pagegood = Paginator(goodList,2).page(pageid)
    newgood = GoodInfo.objects.filter(gtype_id=typeid).order_by('-id')[0:3]
    return render(request, 'df_goods/list.html', {'newgood':newgood,
                                                  'goodList':pagegood,
                                                  'sort':sortid,
                                                  'typeid':typeid})


def detail(request,gid):#这里的gi是前端传过来的值
    g = GoodInfo.objects.get(id=gid)#过滤前端与其匹配的货物信息
    g.gclick = g.gclick + 1
    #点击量加一
    g.save()
    newgood = GoodInfo.objects.filter(gtype_id=g.gtype_id).order_by('-id')[0:3]#相同类型的货物id筛选出来然后排序
    goodtype = g.gtype
    return render(request, 'df_goods/detail.html',{'g': g, 'goodtype':goodtype, 'newgood':newgood})#后面这个字典的key值要与前端对应，
    #后面的值就是自己定义的值


def index(request):
    fruit2 = GoodInfo.objects.filter(gtype=2).order_by('-gclick')[0:4]
    fruit = GoodInfo.objects.filter(gtype=2).order_by('-gclick')[0:4]
    fish2 = GoodInfo.objects.filter(gtype=4).order_by('-gclick')[0:4]
    fish = GoodInfo.objects.filter(gtype=4).order_by('-gclick')[0:4]
    return render(request, 'df_goods/index.html', {'page_name': 1, 'fruit2': fruit2, 'fruit': fruit, 'fish2': fish2, 'fish' :fish})


def search(request):
    fgood = request.GET.get('q')
    gfind = GoodInfo.objects.filter(gtitle__contains=fgood)
    return render(request,'df_goods/list.html',{'goodList':gfind})