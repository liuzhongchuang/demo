from django.shortcuts import render
from login import models

# Create your views here.
from django.shortcuts import HttpResponse

userList = []

"""
第一个参数必须是request,request里面封装了用户的请求信息
返回的时候，不能直接返回字符串，因为要到前端浏览器，走http协议，所以只能用HttpResponse来封装
"""
def index(request):
    # return HttpResponse("hello world")
    if request.method == 'POST':
        uname = request.POST.get("username")
        upassword = request.POST.get("password")
        print(uname, upassword)

        # 将接收到的用户名和密码封装成一个字典，然后返回到前端
        # temp = {'username':uname, 'password':upassword}
        # userList.append(temp)
        # 生成一条数据，增加到数据库
        # models.UserInfo.objects.create(username = uname, password=upassword)
        user = models.UserInfo(username = uname, password=upassword)
        user.save()
    """
    :param request: 这个参数必须是request
    :return: 第二个参数index.html是模版名称
    """
    # 从数据库里面读取数据
    userList = models.UserInfo.objects.all()


    return render(request, 'index.html', {'data':userList})