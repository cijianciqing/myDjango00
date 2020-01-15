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

    # for i in range(1,100):
    #     # print(random.randrange(1,100))
    #     print(''.join(random.sample(string.ascii_letters + string.digits, 4)))

    querysetlist = []
    for i in range(1,1000):
        ranStr = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        ranInt = random.randrange(1,100)
        querysetlist.append(Employee(name=ranStr,age=ranInt,address='homeOf{}'.format(ranStr)))
    Employee.objects.bulk_create(querysetlist)
