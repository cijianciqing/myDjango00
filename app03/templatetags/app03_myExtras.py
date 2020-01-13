#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/13/013 9:17
# software: PyCharm

from django import template

from app02 import models

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.simple_tag
def my_tag(a, b, *args, **kwargs):
    warning = kwargs['warning']
    return "{} {} {}".format(a,b,warning)

@register.inclusion_tag('app03/mySimpleTag.html')
def show_results():
    choices =  models.Publisher.objects.all()
    return {'choices': choices}