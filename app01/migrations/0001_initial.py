# Generated by Django 2.2 on 2020-01-04 01:38

import app01.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to=app01.models.image_upload_to)),
            ],
        ),
    ]
