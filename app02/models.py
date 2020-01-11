from django.db import models


# Create your models here.

# 图书管理系统, 书  作者 出版社


# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的ID主键
    # 创建一个varchar(64)的唯一的不为空的字段
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return "<Publisher Object: {}>".format(self.name)

    def publisher2dict(publisher):
        return {
            'id': publisher.name,
            'name': publisher.name,
            'addr': publisher.addr
        }

    # 书
    class Book(models.Model):
        id = models.AutoField(primary_key=True)  # 自增的ID主键
        # 创建一个varchar(64)的唯一的不为空的字段
        title = models.CharField(max_length=64, null=False, unique=True)
        # 和出版社关联的外键字段
        publisher = models.ForeignKey(to="Publisher", null=True, blank=True, on_delete=models.SET_NULL)

        def __str__(self):
            return "<Book Object: {}>".format(self.title)

    # # 作者表
    class Author(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=16, null=False, unique=True)
        # 告诉ORM 我这张表和book表是多对多的关联关系,ORM自动帮我生成了第三张表
        books = models.ManyToManyField(to="Book")

        def __str__(self):
            return "<Author Object: {}>".format(self.name)
