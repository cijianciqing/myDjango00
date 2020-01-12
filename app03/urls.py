#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView

from . import views

app_name = 'app03'

urlpatterns = [
    # publisher
    path('', TemplateView.as_view(template_name="app03/dashboard.html"),name='app03'),
    path('inherit/', TemplateView.as_view(template_name="app03/inherit.html"),name='inherit'),
    path('publisherList/', views.publisher_list,name='publisherList'),
    path('table00/', TemplateView.as_view(template_name="app03/bootstrapTable00.html"), name='table00'),
    path('table01/', TemplateView.as_view(template_name="app03/bootstrapTable01.html"),name='table01'),
]
