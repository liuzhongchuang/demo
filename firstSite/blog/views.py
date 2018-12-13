from django.db.models import QuerySet
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Blog, Author
from django.http import HttpResponse

# Create your views here.

"""
默认在blog下面显示所有blog信息
"""
def showBlogList(request):
    # 使用loader获取需要渲染的模块
    temp = loader.get_template('blog.html')

    #将数据从数据库里面读取出来
    blogs = Blog.objects.all();
    html = temp.render({'blog':blogs})

    return HttpResponse(html)
    # return render(request, 'blog.html',{'blog':Blog.objects.all()})

def blogInsert(request):
    if request.method == 'POST':
        # 获取参数里面传过来的数据
        u_title = request.POST.get("title")
        u_content = request.POST.get("content")

    # 构建一个博客文章的对象,给默认的作者id赋一个默认值
    blog = Blog(title=u_title,
                content=u_content,
                author_id=2)
    # 将文章内容增加到数据库
    blog.save()
    return render(request, 'blog.html')


def showBlogContent(request, blogId):
    blog = Blog.objects.get(id=blogId)
    return render(request, 'blogDetail.html',{'blog':blog})

@csrf_exempt
def searchBlog(request):
    blogs = []
    u_title = request.POST.get('searchStr')
    # 完全匹配查询数据
    # blog = Blog.objects.get(title=u_title)
    # blogs.append(blog)

    #完全匹配
    # Blog.objects.filter(title=u_title)
    #contains表示包含即可
    # blog = Blog.objects.filter(title__contains=u_title)
    # blog = Blog.objects.filter(title__iendswith=u_title)
    blog = Blog.objects.filter(title__iregex=u_title+'$')


    return render(request, 'blog.html', {'blog': blog})


@csrf_exempt
def searchBlogByAuthor(request):
    # blogs = QuerySet()
    # # 获取查询条件作者名称
    author_name = request.POST.get('authorName')
    # #根据作者名称模糊查询
    # authors = Author.objects.filter(name__contains=author_name)
    # for author in authors:
    #     blogs.union(Blog.objects.filter(author_id=author.id))

    blogs=Blog.objects.filter(author__name__contains=author_name)

    return render(request, 'blog.html', {'blog': blogs})


