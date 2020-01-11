#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/4/004 9:26
# software: PyCharm

from django.contrib import admin
from django.urls import path,include,re_path
from . import views

app_name = 'app02'

urlpatterns = [
    # publisher
    path('publisherList/', views.publisher_list, name='publisherList' ),
    path('add_publisher/', views.add_publisher, name='publisherAdd'),
    path('delete_publisher', views.delete_publisher, name='publisherDelete'),
    path('edit_publisher', views.edit_publisher, name='publisherEdit'),
    # author
    path('authorList/', views.author_list, name='authorList' ),
    path('add_author/', views.add_author, name='authorAdd'),
    path('delete_author', views.delete_author, name='authorDelete'),
    path('edit_author', views.edit_author, name='authorEdit'),
]
