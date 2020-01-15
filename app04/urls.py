#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView

from . import views

app_name = 'app04'

urlpatterns = [
    # publisher
    path('', TemplateView.as_view(template_name="app04/bootstrapTable01.html"), name='app04'),
    path('table01/', TemplateView.as_view(template_name="app04/bootstrapTable01.html"), name='table01'),
    path('table02/', TemplateView.as_view(template_name="app04/bootstrapTable02.html"), name='table02'),
    path('getAllEmployees/', views.getAll,name='getAll'),
]
