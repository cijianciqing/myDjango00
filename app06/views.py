from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def setCookie(request):
    rep = render(request,"app06/basic.html")
    rep.set_cookie('key2','value2')
    return rep

def getCookie(request):
    cookie01 = request.COOKIES['key2']
    print("#"*100)
    print(cookie01)
    print(type(cookie01))
    print("#" * 100)
    return HttpResponse("this is result from getCookie()")

def setCookie02(request):
    rep = redirect("app06:getCookie02")
    rep.set_cookie('key3','value3')
    return rep


def getCookie02(request):
    cookie03 = request.COOKIES['key3']
    print("#"*100)
    print(cookie03)
    print(type(cookie03))
    print("#" * 100)
    return HttpResponse("this is result from getCookie02()")

def setSession(request):
    request.session['k1'] = 'v1'
    rep = render(request,"app06/basicSession.html")
    return rep

def getSession(request):
    session01 = request.session['k1']
    print("#"*100)
    print(session01)
    print(type(session01))
    print("#" * 100)
    return HttpResponse("this is result from getSession()")


def setSession02(request):
    request.session['k2'] = 'v2'
    rep = redirect('app06:getSession02')
    return rep

def getSession02(request):
    session02 = request.session['k2']
    print("#"*100)
    print(session02)
    print(type(session02))
    print("#" * 100)
    return HttpResponse("this is result from getSession02()")