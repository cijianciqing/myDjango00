#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView

from . import views

app_name = 'app05'

urlpatterns = [
    # publisher
    path('', TemplateView.as_view(template_name="app05/login.html"), name='app05'),

    path('basicRegister/', views.basicRegister, name='basicRegister'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('afterLogin/', views.afterLogin, name='afterLogin'),

]
