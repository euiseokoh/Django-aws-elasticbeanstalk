"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


from . import views

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<channel>.+)/checkserverapi/(?P<appname>.+$)', views.CheckSeverAPIwithapp.as_view(), name='checkapi'),
    url(r'^(?P<channel>.+)/checkserverapi/', views.CheckSeverAPI.as_view(), name='checkapi'),
    url(r'^(?P<channel>.+)/index/(?P<appname>.+$)', views.IndexViewwithapp.as_view(), name='checkserver'),
    url(r'^(?P<channel>.+)/index/', views.IndexView.as_view(), name='checkserver'),
    url(r'^(?P<channel>.+)/checkserver/(?P<id>.+$)', views.ContentView.as_view(), name='checkserver'),

)
