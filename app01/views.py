from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MyPerson
import time, logging, os
# Create your views here.

def index(request):
    latest_Person_list = MyPerson.objects.all()[:10]
    myPersonList = {'latest_person_list': latest_Person_list}
    return render(request, 'app01/myPersonList.html', myPersonList)

def detail(request, myPersonID):
    # print( myPersonID)
    myperson = get_object_or_404(MyPerson, pk=myPersonID)
    # question.cho
    return render(request, 'app01/myPersonDetail.html', {'myPerson01': myperson})

#通过模型进行文件上传
# def add(request):
#     if(request.method == 'POST'):
#         #这是文件别名
#         filename=request.POST.get("fileName",default='myFN')
#         files = request.FILES
#         for key, uploaded_file in files.items():
#             myPerson = MyPerson()
#             myPerson.name = filename
#             myPerson.image = uploaded_file
#             myPerson.save()
#         return redirect("myPerson:index")
#     return render(request, 'app01/myPersonAdd.html')

#最简单版本的文件上传
# 处理上传文件的函数
# def add(request):
#     """
#     保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
#     但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         print(request.FILES)
#         #真正的文件名称
#         print(request.FILES["file00"].name)
#         # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
#         filename = request.FILES["file00"].name
#         newFilePah = "myUpload/"+filename
#         # # 在项目目录下新建一个文件
#         with open(newFilePah, "wb") as f:
#             # 从上传的文件对象中一点一点读
#             for i in request.FILES["file00"].chunks():
#                 # 写入本地文件
#                 f.write(i)
#         return HttpResponse("上传OK")
#
#     else:
#         return render(request, 'app01/myPersonAdd.html')


def delete(request,myPersonID):
    myPerson = MyPerson.objects.get(id=myPersonID)
    if (myPersonID):
        myPerson.delete()
        return redirect("myPerson:index")
    return HttpResponse("无法删除！！！！")


def update(request, myPersonID):
    print("sadfasdfasdfasdfasdf")
    myPerson = MyPerson.objects.get(id=myPersonID)
    if (request.method == 'POST'):
        filename = request.POST.get("fileName", default='myFN')
        file = request.FILES.get("file00")
        if(file):
            myPerson.image = file
        myPerson.name = filename
        myPerson.save()
        #此时是否需要reverse()???
        return redirect("myPerson:index")
    return render(request, 'app01/myPersonUpdate.html',{"myPerson": myPerson})
