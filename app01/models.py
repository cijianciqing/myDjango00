from django.db import models

import uuid,time, random, string

from django.db import models


def image_upload_to(instance, filename):
    today = time.strftime("%F")
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    newKey = filename[-20:]
    filename01 = today + "---" + ran_str + "---" + newKey#2011-01-02---2sdxaega---asdfasdfasdfasdfasd.jpg
    return 'weixinFiles/{filename}'.format(filename=filename01)

# Create your models here.
class MyPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.name