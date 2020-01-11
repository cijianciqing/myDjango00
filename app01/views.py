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

def add(request):
    if(request.method == 'POST'):
        filename=request.POST.get("fileName",default='myFN')
        files = request.FILES
        for key, uploaded_file in files.items():
            myPerson = MyPerson()
            myPerson.name = filename
            myPerson.image = uploaded_file
            myPerson.save()
        return redirect("myPerson:index")
    return render(request, 'app01/myPersonAdd.html')


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
        return redirect("myPerson:index")
    return render(request, 'app01/myPersonUpdate.html',{"myPerson": myPerson})
