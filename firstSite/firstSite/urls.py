"""firstSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
from polls import views as pView
from blog import views as bView
from django.conf.urls import include, url
from area import views as aview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.index),
    url(r'^$', pView.index),
    url(r'^polls/', include('polls.urls')),

    url(r'^blog$', bView.showBlogList),
    url(r'blogInsert/$', bView.blogInsert),
    url(r'^blog/(?P<blogId>[0-9]+)/$', bView.showBlogContent),
    url(r'^searchBlog/$', bView.searchBlog),
    url(r'^searchBlogByAuthor/$', bView.searchBlogByAuthor),
    url(r'^area$', aview.area),
    url(r'^area/(\d+)$',aview.bindArea),
    url(r'^fileUpload$',aview.fileUpload),
    url(r'^fileUploadHandle$',aview.fileUploadHandle)
]
