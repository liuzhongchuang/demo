
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from gevent.libev.corecext import os

from area.models import AreaInfo
from firstSite import settings

'''
跳转到省界面
'''
def area(request):
    return render(request,'area.html')


def bindArea(request,id):
    areas = AreaInfo.objects.filter(parea_id=id)
    areaList = []
    for area in areas:
        areaList.append([area.id,area.title])
    return JsonResponse({'data':areaList})

'''
跳转到上传文件的界面
'''
def fileUpload(request):
    return render(request,'fileupload.html')


'''
处理文件上传
'''
def fileUploadHandle(request):
    file1 = request.FILES['file1']
    #将选择的文件内容读取到content里
    content = file1.read()
    fileName =os.path.join(settings.MEDIA_ROOT,file1.name)
    with open(fileName,'wb') as f1:
        f1.write(content)
        return HttpResponse('上传成功')