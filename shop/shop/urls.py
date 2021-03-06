"""shop URL Configuration

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
from django.conf.urls import include, url
from df_goods import views as gviews
urlpatterns = [
    path('^admin/', admin.site.urls),
    # url(r'^$', gviews.index),
    url(r'^user/', include('df_user.urls')),
    url(r'^cart/', include('df_cart.urls')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^', include('df_goods.urls')),
    # url(r'^search/',include('df_goods.urls'))
    # url(r'\d+/$', gviews.detail),

    url(r'^order/', include('df_order.urls')),
    # url(r'^', include('df_goods.urls', 'goods'), namespace='goods'),
]
