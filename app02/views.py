from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app02 import models

import time, logging, os
# Create your views here.

def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "app02/publisher/publisher_list.html", {"publisher_list": ret})


# 添加新的出版社
def add_publisher(request):
    error_msg = ""
    # 如果是POST请求,我就取到用户填写的数据
    if request.method == "POST":
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("app02:publisherList")
        else:
            error_msg = "出版社名字不能为空!"
    # 用户第一次来,我给他返回一个用来填写的HTML页面
    return render(request, "app02/publisher/add_publisher.html", {"error": error_msg})


# 删除出版社的函数
def delete_publisher(request):
    print(request.GET)
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        return redirect("app02:publisherList")
    else:
        return HttpResponse("要删除的数据不存在!")


# 编辑出版社
def edit_publisher(request):
    # 用户修改完出版社的名字,点击提交按钮,给我发来新的出版社名字
    if request.method == "POST":
        print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        # 更新出版社
        # 根据id取到编辑的是哪个出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()  # 把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        return redirect("app02:publisherList")
    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("id")
    if edit_id:
        # 获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "app02/publisher/edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在!")


def author_list(request):
    author_list = models.Author.objects.all()
    return render(request,'app02/author/author_list.html',context={"author_list": author_list})


def add_author(request):
    books = models.Book.objects.all()
    if request.method == 'POST':
        authorName = request.POST.get("author_name",'testAuthorName')
        # post提交的数据是多个值的时候一定会要用getlist,如多选的checkbox和多选的select
        books = request.POST.getlist("books")

        #以下是错误用法
        # author01 = models.Author()
        # author01.name = authorName
        author01 = models.Author.objects.create(name=authorName)
        author01.books.set(books)
        return redirect(to='app02:authorList')
    return render(request,'app02/author/add_author.html',context={"book_list": books})


def delete_author(request):
    authorId = request.GET.get('id')
    models.Author.objects.get(id=authorId).delete()
    return redirect(to='app02:authorList')


def edit_author(request):
    books = models.Book.objects.all()
    if request.method == 'POST':
        authorId = request.POST.get('author_id')
        authorName = request.POST.get("author_name", 'testAuthorName')
        # post提交的数据是多个值的时候一定会要用getlist,如多选的checkbox和多选的select
        books = request.POST.getlist("books")
        author = models.Author.objects.get(pk=authorId)
        author.name = authorName
        author.books.set(books)
        return redirect(to='app02:authorList')
    authorId = request.GET.get('id')
    author = models.Author.objects.get(id = authorId)
    return render(request,'app02/author/edit_author.html',context={'author': author,'book_list': books})