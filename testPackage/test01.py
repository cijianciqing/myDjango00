#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/13/013 17:47
# software: PyCharm
import os

if __name__ == '__main__':
    #加载配置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjango00.settings')
    # 启动django
    import django
    django.setup()

    from app01 import models

    result = models.MyPerson.objects.all()
    print(result)