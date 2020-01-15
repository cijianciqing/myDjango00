import os
import django
import logging

from django.core import serializers
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjango00.settings')
django.setup()





if __name__ == '__main__':
    from app02.models import *
    ret = Publisher.objects.all()
    ret1 = serializers.serialize("json", ret)
    print(type(ret1))
    print(ret1)
    ret2 = json.loads(ret1)
    print(type(ret2))
    print(ret2)
