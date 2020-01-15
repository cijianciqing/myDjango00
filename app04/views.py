from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from app04 import models


def getAll(request):
    print(request.method)
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    queryset = models.Employee.objects.all()
    responseData = []
    for employee in queryset:
        employeeJson = employee.employee2dict()
        responseData.append(employeeJson)
    print(responseData)
    return JsonResponse({"rows": responseData})