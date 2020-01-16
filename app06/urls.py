#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView

from . import views

app_name = 'app06'

urlpatterns = [


    path('setCookie',views.setCookie,name='setCookie'),
    path('getCookie', views.getCookie, name='getCookie'),

    path('setCookie02',views.setCookie02,name='setCookie02'),
    path('getCookie02', views.getCookie02, name='getCookie02'),

    path('setSession',views.setSession,name='setSession'),
    path('getSession', views.getSession, name='getSession'),

    path('setSession02',views.setSession02,name='setSession02'),
    path('getSession02', views.getSession02, name='getSession02'),

]
