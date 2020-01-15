import os
import django






if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjango00.settings')
    django.setup()

    import logging
    from app04.models import Employee
    import uuid
    import random
    import string

    from app02.models import Publisher, Book, Author

    # values  values_list
    # aa = Publisher.objects.values_list("name")
    # aa = Publisher.objects.values("name")
    # print(type(aa))
    # print(aa)
    # < QuerySet[{'name': 'adfasdfasdf'}, {'name': 'publisher0002'}, {'name': 'publisher0003'}] >



    # 聚合  aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。
    from django.db.models import Avg, Sum, Max, Min, Count
    #          # Book.objects.all().aggregate(Avg("price"))
    # bb= Publisher.objects.all().aggregate(Count("name"))
    # print(type(bb))
    # print(bb)

    # 分组