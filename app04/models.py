from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

    def employee2dict(employee):
        return {
            'id': employee.id,
            'name': employee.name,
            'age': employee.age,
            'address': employee.address
        }