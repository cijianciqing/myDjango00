from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from .myRegisterForm import RegForm, SimpleRegForm

def basicRegister(request):
    form_obj = SimpleRegForm()
    if request.method == "POST":
        form_obj = SimpleRegForm(request.POST)
        print("+--" * 100)
        print(form_obj)
        print("+--" * 100)
        if form_obj.is_valid():
            print("+" * 100)
            print(form_obj.cleaned_data)
            print("+" * 100)
            username = request.POST["name"]
            password = request.POST["pwd"]
            user = User.objects.create_user(username=username, password=password)
            return render(request, "app05/login.html")
    return render(request, "app05/simpleRegister.html", {"form_obj": form_obj})


def register(request):
    form_obj = RegForm()
    if request.method=="POST":
        form_obj = RegForm(request.POST)

        if form_obj.is_valid():
            print("+" * 100)
            print(form_obj.cleaned_data)
            print("+" * 100)
            username = request.POST["name"]
            password = request.POST["pwd"]
            email = request.POST["pwd"]
            user = User.objects.create_user(username=username,password=password,email=email)
            return render(request,"app05/login.html")

    return render(request, "app05/register.html", {"form_obj": form_obj})


def login(request):
    if request.method=="GET":
        next_url = request.GET.get("next")
        # print("@!" * 100)
        # print(request.get_full_path())
        # print(next_url)
        # print("@!" * 100)
        # 在session中设置需要重定向的url
        request.session['afterLoginURL'] = next_url
        return render(request,"app05/login.html")

    #从session中获取重定向地址
    # next_url = request.POST.get("next")
    my_next_url = request.session['afterLoginURL']
    # print("!" * 100)
    # print(my_next_url)
    # print("!" * 100)

    username = request.POST["inputEmail"]
    password = request.POST["inputPassword"]
    user_obj = auth.authenticate(username= username, password=password)
    if user_obj:
        print("@" * 100)
        print(username,"authenticated")
        print( "@"*100)
        # 该函数实现一个用户登录的功能。它本质上会在后端为该用户生成相关session数据
        auth.login(request, user_obj)
        #认证成功后重定向到特定地址或者用户之前的地址
        if my_next_url:
            rep = redirect(my_next_url)  # 得到一个响应对象
        else:
            rep = redirect("/")  # 得到一个响应对象
        return rep
    return redirect("app05:login")

@login_required
def afterLogin(request):
    # print("$"*100)
    # print(request.user)
    # print("$" * 100)
    return HttpResponse("afterLogin OK")


