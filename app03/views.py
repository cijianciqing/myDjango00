from django.shortcuts import render
from django.http import JsonResponse
from app02 import models
import json
# Create your views here.

def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    queryset = models.Publisher.objects.all()
    responseData = []
    for publisher in queryset:
        publisherJson = publisher.publisher2dict()
        responseData.append(publisherJson)
    print(responseData)
    return JsonResponse({"rows": responseData})