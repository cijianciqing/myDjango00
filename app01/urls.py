#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from . import views

app_name = 'myPerson'

urlpatterns = [
    # 查询 get
    path('', views.index, name='index'),
    path('getOne/<int:myPersonID>/', views.detail, name='detail'),
    # 新增 get + post
    path('add/', views.add, name='add'),
    # 删除 get
    path('delete/<int:myPersonID>/', views.delete, name='delete'),
    # 修改 get + post
    path('update/<int:myPersonID>/', views.update, name='update'),
    # re_path('update/<int:myPersonID>', views.update, name=''),
    # re_path('update/(?P<myPersonID>\d+)/', views.update, name='update'),
    # path('update/2/', views.update00, name='update00'),
]
