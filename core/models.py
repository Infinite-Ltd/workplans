from django.db import models

# Create your models here.

#userinfo entity


class Userinfo(models.Model):
    #guid = models.CharField(max_length=30)
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    register_date = models.CharField(max_length=12)
    aliasName = models.CharField(max_length=15)
    employeeId = models.CharField(max_length=8)
    isleader = models.BooleanField(default=False)
    dirLeader = models.CharField(max_length=20, default='陈清洲')

class Workplan(models.Model):
    user = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    index = models.CharField(max_length=5)
    comment = models.CharField(max_length=300)

